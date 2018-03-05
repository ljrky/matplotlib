"""
设置图像窗口的名字和大小
设置曲线的颜色，宽度，类型(比如点状线)
"""

import numpy as np
import matplotlib.pyplot as plt

# 生成线性数据
x = np.linspace(-3,3,50)

# 定义一个线性函数
y1 = 2 * x + 1

# 定义一个非线性函数
# y2 = x**2
y2 = np.sin(x)

# 定义图像窗口
plt.figure()

# 画线性函数曲线,并显示
plt.plot(x,y1)
plt.show()

# 画非线性函数曲线,并显示
plt.plot(x,y2)
plt.show()

# 线性和非线性画在一起,并显示
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()

# 设置图像窗口的名字(在左上角)，和大小 : plt.figure(num=3, figsize=(8,5),)
# 曲线颜色，宽度，类型 : plt.plot(x,y2,color='red',linewidth=5.0,linestyle='--')
plt.figure(num=3, figsize=(8,5),)
plt.plot(x,y1)
plt.plot(x,y2,color='red',linewidth=5.0,linestyle='--')
plt.show()


