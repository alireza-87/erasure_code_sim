from heapq import heappush

import constant as cnt
from exceptions import SystemFail
from modules.upload_download.download_complete import DownloadComplete
from modules.node import NodeFail
from modules.node import NodeOffline
from modules.server import ServerFail
from modules.server import ServerOffline
from modules.upload_download.upload_complete import UploadComplete
from utilities import exp_rv


class State:
    current_k = 0
    time_upload = 0
    time_download = 0
    item_k = 0

    def __init__(self, t_u, t_d, k):
        self.t = t = 0  # seconds
        self.time_upload = t_u
        self.time_download = t_d
        self.item_k = k
        self.node_online = True  # the node starts online
        self.server_online = [True] * cnt.N  # servers all start online
        self.remote_blocks = [False] * cnt.N
        if not cnt.B == 1:
            for i in range(len(self.remote_blocks)):
                self.remote_blocks[i] = [False] * cnt.B
        # if cnt.B == 1:
        #    self.remote_blocks = [False] * cnt.N
        # else:
        #    self.remote_blocks = [[False] * cnt.B] * cnt.N  # no server starts having their block
        self.local_blocks = [True] * cnt.N  # flags each locally owned block

        self.current_upload = self.current_download = None
        self.events = []  # event queue

        self.schedule(exp_rv(cnt.NODE_UPTIME), NodeOffline())
        self.schedule(exp_rv(cnt.NODE_LIFETIME), NodeFail())
        for i in range(cnt.N):
            self.schedule(exp_rv(cnt.SERVER_UPTIME), ServerOffline(i))
            self.schedule(exp_rv(cnt.SERVER_LIFETIME), ServerFail(i))
        self.schedule_next_upload()

    def schedule(self, delay, event):
        """Add an event to the event queue after the required delay."""
        heappush(self.events, (self.t + delay, event))

    def schedule_next_upload(self):
        """Schedule the next upload, if any."""
        if self.node_online:
            if cnt.B == 1:
                for i in range(0, cnt.N):
                    if self.local_blocks[i] and self.server_online[i] and not self.remote_blocks[i]:
                        self.current_upload = UploadComplete(i,0)
                        self.schedule(exp_rv(self.time_upload), self.current_upload)
            else:
                for i in range(0, cnt.N):
                    for j in range(0, cnt.B):
                        if self.local_blocks[i] and self.server_online[i] and not self.remote_blocks[i][j]:
                            self.current_upload = UploadComplete(i, j)
                            self.schedule(exp_rv(self.time_upload), self.current_upload)

        # if the node is online, upload a possessed local block to an online
        # server that doesn't have it (if possible)

    def schedule_next_download(self):
        """Schedule the next download, if any."""
        if self.node_online:
            for i in range(cnt.N):
                if not cnt.B == 1:
                    for j in range(0, cnt.B):
                        if self.remote_blocks[i][j] and self.server_online[i] and not self.local_blocks[i]:
                            self.current_download = DownloadComplete(i)
                            self.schedule(exp_rv(self.time_download), self.current_download)
                else:
                    if self.remote_blocks[i] and self.server_online[i] and not self.local_blocks[i]:
                        self.current_download = DownloadComplete(i)
                        self.schedule(exp_rv(self.time_download), self.current_download)

        # if the node is online, download a remote block the node doesn't
        # have from an online server which has it (if possible)

    def check_game_over(self):
        """Did we lose enough redundancy that we can't recover data?"""
        # check if we have at least K blocks saved, either locally or remotely
        if cnt.B == 1:
            lbs, rbs = self.local_blocks, self.remote_blocks
            blocks_saved = [lb or rb for lb, rb in zip(lbs, rbs)]
            if sum(blocks_saved) < self.item_k:
                raise SystemFail()
        else:
            lbs, rbs = self.local_blocks, self.remote_blocks
            result = []
            for i in rbs:
                result.append(any(i))
            blocks_saved = [lb or rb for lb, rb in zip(lbs, result)]
            if sum(blocks_saved) < self.item_k:
                raise SystemFail()
