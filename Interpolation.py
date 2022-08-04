# -*-coding:utf-8 -*-
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from scipy import interpolate
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pylab as pl

x = np.linspace(0, 10, 11)
# x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
y = np.sin(x)
xnew = np.linspace(0, 10, 1001)  # 注意这里不能超过上面x给定的范围
pl.plot(x, y, "ro")

for kind in ["nearest", "zero", "slinear", "quadratic", "cubic"]:  # 插值方式
    # "nearest","zero"为阶梯插值
    # slinear 线性插值
    # "quadratic","cubic" 为2阶、3阶B样条曲线插值
    f = interpolate.interp1d(x, y, kind=kind)  # 通过这几个就能计算出来具体的函数的参数hhh, 然后再加入自变量就能给出y的值
    # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
    ynew = f(xnew)
    pl.plot(xnew, ynew, label=str(kind))
pl.legend(loc="lower right")
pl.show()

"""
演示二维插值。
"""


def func(x, y):
    return (x + y) * np.exp(-5.0 * (x ** 2 + y ** 2))


# X-Y轴分为15*15的网格
y, x = np.mgrid[-1:1:15j, -1:1:15j]
# 始终没弄明白里面逻辑, 之后感谢try:语法解释https://blog.csdn.net/KangLongWang/article/details/102811162
print(x, '\n', np.linspace(-1, 1, 15))

fvals = func(x, y)  # 计算每个网格点上的函数值  15*15的值
print(len(fvals[0]))

# 三次样条二维插值
newfunc = interpolate.interp2d(x, y, fvals, kind='cubic')

# 计算100*100的网格上的插值
xnew = np.linspace(-1, 1, 100)  # x
ynew = np.linspace(-1, 1, 100)  # y
fnew = newfunc(xnew, ynew)  # 仅仅是y值   100*100的值

# 绘图
# 为了更明显地比较插值前后的区别，使用关键字参数interpolation='nearest'
# 关闭imshow()内置的插值运算。
pl.subplot(121)
im1 = pl.imshow(fvals, extent=[-1, 1, -1, 1], cmap=mpl.cm.hot, interpolation='nearest', origin="lower")  # pl.cm.jet
# extent=[-1,1,-1,1]为x,y范围  favals为 单纯就是硬划分
pl.colorbar(im1)

pl.subplot(122)
im2 = pl.imshow(fnew, extent=[-1, 1, -1, 1], cmap=mpl.cm.hot, interpolation='nearest',
                origin="lower")  # origin="lower"没懂
pl.colorbar(im2)
pl.show()

# X-Y轴分为20*20的网格
x = np.linspace(-1, 1, 20)
y = np.linspace(-1, 1, 20)
x, y = np.meshgrid(x, y)  # 20*20的网格数据

fvals = func(x, y)  # 计算每个网格点上的函数值  15*15的值

fig = plt.figure(figsize=(9, 6))
# Draw sub-graph1
ax = plt.subplot(1, 2, 1, projection='3d')
surf = ax.plot_surface(x, y, fvals, rstride=4, cstride=2, cmap=cm.coolwarm, linewidth=0.5, antialiased=True)
ax.set_xlabel('x')  # 上面的rstride啥的就是控制网格, 但是具体不太明白是怎么控制的, 可能是几个点合成成一个格子
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.colorbar(surf, shrink=0.5, aspect=5)  # 标注

# 二维插值
newfunc = interpolate.interp2d(x, y, fvals, kind='cubic')  # newfunc为一个函数

# 计算100*100的网格上的插值
xnew = np.linspace(-1, 1, 100)  # x
ynew = np.linspace(-1, 1, 100)  # y
fnew = newfunc(xnew, ynew)  # 仅仅是y值   100*100的值  np.shape(fnew) is 100*100
xnew, ynew = np.meshgrid(xnew, ynew)
ax2 = plt.subplot(1, 2, 2, projection='3d')
surf2 = ax2.plot_surface(xnew, ynew, fnew, rstride=2, cstride=2, cmap=cm.coolwarm, linewidth=0.5, antialiased=True)
ax2.set_xlabel('xnew')
ax2.set_ylabel('ynew')
ax2.set_zlabel('fnew(x, y)')
plt.colorbar(surf2, shrink=100, aspect=5)  # 标注

plt.show()