import constant as cnt
from utilities import exp_rv


class ServerEvent:
    """Class with a self.server attribute."""

    def __init__(self, server):
        self.server = server

    def __str__(self):  # function to get a pretty printed name for the event
        return f'{self.__class__.__name__}({self.server})'


class ServerOnline(ServerEvent):
    """A server that was offline went back online."""

    def process(self, state):
        server = self.server
        state.server_online[server] = True  # mark the server as back online
        state.schedule(exp_rv(cnt.SERVER_UPTIME), ServerOffline(server))  # schedule the next server offline event
        # if the node was not uploading/downloading,
        # schedule new uploads/downloads to/from them
        cu = state.current_upload
        cd = state.current_download
        if cu is not None:
            state.schedule_next_upload()
        if cd is not None:
            state.schedule_next_download()


class ServerOffline(ServerEvent):
    """A server went offline."""

    def process(self, state):
        server = self.server
        # mark the server as offline
        state.server_online[server] = False
        # schedule the next server online event
        state.schedule(exp_rv(cnt.SERVER_DOWNTIME), ServerOnline(server))
        # interrupt any current uploads/downloads to this server
        cu = state.current_upload
        if cu is not None and cu.server == server:
            state.current_upload = None
        cd = state.current_download
        if cd is not None and cd.server == server:
            state.current_download = None


class ServerFail(ServerOffline):
    """A server failed and lost its data."""

    def process(self, state):
        state.remote_blocks[self.server] = [False] * cnt.B
        state.check_game_over()
        state.schedule(exp_rv(cnt.SERVER_LIFETIME), ServerFail(self.server))
        super().process(state)
