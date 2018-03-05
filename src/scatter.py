"""
散点图
"""

import matplotlib.pyplot as plt
import numpy as np

n = 1024
# 1024个平局值为0，方差为1的数据集
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)

# 设置散点图的点的大小，点的颜色和点的透明度
plt.scatter(X,Y,s=75,c=T,alpha=0.5)
# 设置坐标系范围和去掉刻度的值
plt.xlim(-1.5,1.5)
plt.xticks()
plt.ylim(-1.5,1.5)
plt.yticks()
plt.show()