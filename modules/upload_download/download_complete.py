import constant as cnt
from modules.server import ServerEvent


class DownloadComplete(ServerEvent):
    """A download is completed."""

    def process(self, state):
        if state.current_download is not self:
            # download interrupted
            return
        lb = state.local_blocks
        lb[self.server] = True
        if sum(lb) >= state.item_k:  # we have enough data to reconstruct all blocks
            state.local_blocks = [True] * cnt.N
        else:
            state.schedule_next_download()
