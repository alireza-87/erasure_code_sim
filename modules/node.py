import constant as cnt
from utilities import exp_rv


class NodeOnline:
    """Our node went online."""

    def process(self, state):
        state.node_online = True  # mark the node as online
        state.schedule_next_upload()  # schedule next upload
        state.schedule_next_download()  # schedule next download
        state.schedule(exp_rv(cnt.NODE_UPTIME), NodeOffline())  # schedule the next offline event


class NodeOffline:
    """Our node went offline."""

    def process(self, state):
        state.node_online = False  # mark the node as offline
        state.current_upload = state.current_download = None  # cancel current upload and download
        state.schedule(exp_rv(cnt.NODE_DOWNTIME), NodeOnline())  # schedule the next online event


class NodeFail(NodeOffline):
    """Our node failed and lost all its data."""

    def process(self, state):
        # mark all local blocks as lost
        state.local_blocks = [False] * cnt.N
        state.check_game_over()
        state.schedule(exp_rv(cnt.NODE_LIFETIME), NodeFail())
        super().process(state)
