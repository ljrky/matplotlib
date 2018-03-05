import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 首先生成一个三维图像
fig = plt.figure()
ax = Axes3D(fig)
# plt.show()

# 生成数据
# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)

# 生成3D图像
# rstride 分别代表row的跨度
# cstride 分别代表column的跨度
# cmap=plt.get_cmap('summer')设置图像的色彩
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
plt.show()