"""
- 设置坐标轴名字，范围
- 设置坐标轴刻度大小，刻度类型，刻度的名字
- 设置图像的边框和颜色
- 设置坐标轴的刻度值的位置
- 设置X坐标轴相对Y坐标轴的相对位置
- 给图像的线条添加注释
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2= x**2

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=2.0,linestyle='--')

# 设置XY坐标的名称和坐标范围
plt.xlim(-1,2)
plt.xlabel('I am x')
plt.ylim(-2,3)
plt.ylabel('I am y')
# plt.show()


# 设置刻度范围，注意要下面的刻度度数的起点一致
plt.xlim(-1,2)
plt.xlabel('I am x')
plt.ylim(-2,3)
plt.ylabel('I am y')
# 设置X轴的刻度为0.6一个刻度
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
# 设置Y轴的刻度为一个数组，并为每个刻度重新命名
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
# 设置线条的名字
plt.plot(x,y2,label='linear line')
plt.plot(x,y1,color='red',linewidth=2.0,linestyle='--',label='square line')
# plt.show()

# 设置图像的边框和颜色
# 获取当前坐标轴信息
ax = plt.gca()
ax.spines['right'].set_color('red')
ax.spines['top'].set_color('green')
# plt.show()

# 设置坐标轴的刻度值的位置
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position('left')
# 设置X坐标轴相对Y坐标轴的相对位置: outward, axes, data
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_position(('data',0))
# plt.show()