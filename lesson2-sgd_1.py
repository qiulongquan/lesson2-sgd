from fastai.basics import *
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import numpy as np


n = 100
x = torch.ones(n, 2)
x[:, 0].uniform_(-1., 1)
print(x[:5])

a = tensor(3., 2)
y = x@a + torch.rand(n)
print(y[:5])

plt.scatter(x[:, 0], y)
print(x[:5])


def mse(y_hat, y):
    return ((y_hat-y)**2).mean()


a = tensor(-1.,1)
y_hat = x@a
mse(y_hat, y)

print(y_hat)

plt.scatter(x[:, 0], y)
plt.scatter(x[:, 0], y_hat)
plt.show()

print("="*50)
a = nn.Parameter(a)


def update():
    y_hat = x@a
    loss = mse(y, y_hat)
    if t % 10 == 0:
        print(loss)
    loss.backward()
    with torch.no_grad():
        a.sub_(lr * a.grad)
        a.grad.zero_()


lr = 1e-1
for t in range(100):
    update()


plt.scatter(x[:, 0], y)
plt.scatter(x[:, 0], x@a)
plt.show()

# animation的部分无法实现，还需要测试。
# 现在动画部分还不能使用。

# from matplotlib import animation as anm, rc
# rc('animation', html='jshtml')
#
# a = nn.Parameter(tensor(-1., 1))
#
# fig = plt.figure()
# plt.scatter(x[:, 0], y, c='orange')
# line, = plt.plot(x[:, 0], x@a)
# plt.close()


# def animate(i):
#     update()
#     line.set_ydata(x@a)
#     return line,


# ani = anm.FuncAnimation(fig, animate, np.arange(0, 100), interval=100)

# ani.save("Sample_sgd.gif", writer='imagemagick')
#
# plt.show()


