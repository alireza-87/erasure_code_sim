from modules.server import ServerEvent
import constant as cnt

class UploadComplete(ServerEvent):
    """An upload is completed."""

    def __init__(self, server, block):
        super().__init__(server)
        self.block = block

    def process(self, state):
        if state.current_upload is not self:
            # this upload was interrupted, we ignore this event
            return
        if cnt.B == 1:
            state.remote_blocks[self.server] = True
        else:
            for i in range(0, self.server):
                state.remote_blocks[i][self.block] = True
        state.schedule_next_upload()
