import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# 可以运动的gif或者mp4文件生成


def f(x, y):
    return np.sin(x) + np.cos(y)


x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
ims = []

fig, [ax1, ax2] = plt.subplots(2, 1)

for i in range(60):
    x += np.pi / 15.
    y += np.pi / 20.
    img1 = ax1.imshow(f(x, y), animated=True)
    img2 = ax2.imshow(f(x, y), animated=True)
    ims.append([img1, img2])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)
ani.save('anim.gif', writer="imagemagick")
# ani.save('anim.mp4', writer="ffmpeg")
plt.show()
