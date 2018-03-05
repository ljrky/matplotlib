"""
将多个小图合成显示为一个大图，有2种方法
- plt.subplot2grid((3, 3), (0, 0), colspan=3)
- plt.subplot(2,2,1)
"""

import matplotlib.pyplot as plt

plt.figure()

# 使用subplot来创建小图，plt.subplot(2,2,1)表示将整个图像窗口分为2行2列, 当前位置为1
# 每画一个小图都要告诉目前是第几个图
# 第1个图
plt.subplot(2,2,1)
plt.plot([0,1],[0,1])

# 第2个图
plt.subplot(2,2,2)
plt.plot([0,1],[0,2])

# 第3个图
plt.subplot(2,2,3)
plt.plot([0,1],[0,3])

# 第4个图
plt.subplot(2,2,4)
plt.plot([0,1],[0,4])

# plt.show()

# 大小不均匀的多个图片
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])

# 这里位置为4是因为，这个命令重新分配了的位置，现在每行有3个，所以第二行一开始就是第4个
plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

# 第3张图
plt.subplot(235)
plt.plot([0,1],[0,3])

# 第4张图
plt.subplot(236)
plt.plot([0,1],[0,4])

plt.show()