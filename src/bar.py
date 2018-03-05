import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)

Y1 =  (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

# 生成两组柱状图，第一个向上，第二个向下
# plt.bar(X,+Y1)
# plt.bar(X,-Y1)

# 设置坐标系范围和去掉刻度
plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())
# plt.show()

# 设置柱状的颜色和边框的颜色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
# plt.show()

# 设置柱状的文字描述
for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x, -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.show()