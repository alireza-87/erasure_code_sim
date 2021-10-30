from modules.server import ServerEvent


class UploadComplete(ServerEvent):
    """An upload is completed."""
    def __init__(self, server, block):
        super().__init__(server)
        self.block = block

    def process(self, state):
        if state.current_upload is not self:
            # this upload was interrupted, we ignore this event
            return
        state.remote_blocks[self.server][self.block] = True
        state.schedule_next_upload()
