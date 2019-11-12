import matplotlib.animation as anm
import matplotlib.pyplot as plt
import numpy as np

# 可以运动的gif文件生成

fig = plt.figure(figsize=(10, 6))
x = np.arange(0, 10, 0.1)


def update(i, fig_title, a):
    if i != 0:
        plt.cla()                      # 現在描写されているグラフを消去

    y = a * np.sin(x - i)
    plt.plot(x, y, "r")
    plt.title(fig_title + 'i=' + str(i))


ani = anm.FuncAnimation(fig, update, fargs=('Initial Animation! ', 2.0), \
    interval=100, frames=132)

ani.save("Sample.gif", writer='imagemagick')
