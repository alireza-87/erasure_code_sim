import matplotlib.pyplot as plt
import numpy as np
import itertools
import constant as cnt
from modules.colors import Colors


def plot_life_time(data_to_plot, title):
    print("data to plot", data_to_plot)
    data_size_label = []
    for i in range(0, len(cnt.DATA_SIZE)):
        plt.plot(cnt.K, list(data_to_plot.values())[i], color=np.random.rand(3, ))
        data_size_label.append(str(cnt.DATA_SIZE[i] / cnt.GB) + "GB")
    plt.legend(data_size_label)
    plt.title(title)
    plt.xticks(cnt.K)
    plt.yticks(list(range(0, 10)))
    plt.xlabel('K', fontsize=12)
    plt.ylabel('Life Time', fontsize=12)
    plt.show()


def plot_fail(data_to_plot, title):
    print(f"{Colors.OKGREEN}data to plot {data_to_plot}{Colors.ENDC}")
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel('K')
    ax.set_ylabel('Number of Game Overs')
    u_d_list = []
    for d_s, u_s in itertools.product(cnt.DOWNLOAD_SPEED_LABEL, cnt.UPLOAD_SPEED_LABEL):
        u_d_list.append('D:' + d_s + ',U:' + u_s)
    color_list = []
    for item_u_d in u_d_list:
        color_list.append(np.random.rand(3, ))
    for x, y in data_to_plot.items():
        h1 = 0.5
        color_index = 0
        bars = []
        for item in y:
            bars.append(ax.bar((x - h1), item, 0.3, color=color_list[color_index], label=u_d_list[color_index]))
            h1 = h1 - 0.1
            color_index = color_index + 1
    ax.set_xticks(list(data_to_plot.keys()))
    ax.set_yticks(list(range(1, cnt.NUMBER_OF_ITERATION+1)))
    ax.legend(handles=bars)
    fig.tight_layout()
    plt.show()
