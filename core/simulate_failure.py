import itertools
from heapq import heappop

import constant as cnt
from exceptions import SystemFail
from core.state import State
from plots import plot


def sim_failure():
    for item_data in cnt.DATA_SIZE:
        print('data size : ', item_data / cnt.GB)
        fails_list = {}
        for item_k in cnt.K:
            fail = []
            print('k : ', item_k)
            for item_d, item_u in itertools.product(cnt.DOWNLOAD_SPEED, cnt.UPLOAD_SPEED):
                print('upload : ', item_u, ' , download : ', item_d)
                fail_count = 0
                block_size = item_data / item_k
                time_upload = block_size / item_u
                time_download = block_size / item_d
                for i in range(cnt.NUMBER_OF_ITERATION + 1):
                    try:
                        state_current = State(time_upload, time_download, item_k)
                        event_queue = state_current.events
                        while event_queue:
                            time, event = heappop(event_queue)
                            if time > cnt.MAXT:
                                break
                            state_current.t = time
                            event.process(state_current)
                    except SystemFail:
                        fail_count = fail_count + 1
                fail.append(fail_count)
            fails_list[item_k] = fail
        plot.plot_fail(fails_list, 'data size : ' + str(item_data / cnt.GB))
