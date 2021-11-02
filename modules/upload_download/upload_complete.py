from modules.server import ServerEvent
import constant as cnt


class UploadComplete(ServerEvent):
    """An upload is completed."""

    def __init__(self, server, block):
        super().__init__(server)
        self.block = block

    def process(self, state):
        if state.current_upload is not self:  # interrupted
            return
        if cnt.B == 1:
            state.remote_blocks[self.server] = True
            state.schedule_next_upload()
        else:
            for i in range(0, self.server):
                state.remote_blocks[i][self.block] = True
            state.schedule_next_upload()
