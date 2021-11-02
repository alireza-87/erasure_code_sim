import itertools
from heapq import heappop

import constant as cnt
from exceptions import SystemFail
from core.state import State
from plots import plot
from modules.colors import Colors


def sim_life_time():
    for item_d, item_u in itertools.product(cnt.DOWNLOAD_SPEED, cnt.UPLOAD_SPEED):
        print(f'{Colors.WARNING}upload : {item_u}, download : {item_d}{Colors.ENDC}')
        life_time = {}
        for item_data in cnt.DATA_SIZE:
            print(f'{Colors.OKCYAN}data size : {item_data / cnt.GB}{Colors.ENDC}')
            times = []
            for item_k in cnt.K:
                print(f'{Colors.OKCYAN}k : {item_k}{Colors.ENDC}')
                block_size = item_data / item_k
                time_upload = block_size / item_u
                time_download = block_size / item_d
                temp = []
                for i in range(cnt.NUMBER_OF_ITERATION + 1):
                    try:
                        state = State(time_upload, time_download, item_k)
                        events = state.events
                        while events:
                            t, event = heappop(events)
                            if t > cnt.MAXT:
                                break
                            state.t = t
                            event.process(state)
                    except SystemFail:
                        pass
                    finally:
                        temp.append(state.t / cnt.YEAR)
                times.append(sum(temp))
            life_time[item_data / cnt.GB] = times
        plot.plot_life_time(life_time, 'D:' + str(item_d/cnt.MB) + ',U:' + str(item_u/cnt.MB))
