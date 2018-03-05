import matplotlib.pyplot as plt
import numpy as np

# 设置x,y
x = np.linspace(-1,1,50)
y = 2 * x + 1

print(x)
print(y)

# 启动图像窗口
plt.figure()
# 把数据x,y传给plt画图
plt.plot(x,y)
# 显示图
plt.show()

# 画一条直线，给出X，Y点的坐标就可以了
x0 = 1
y0 = 2 * x0 + 1
plt.figure(figsize=(8,5))
plt.xlim(-1,10)
plt.ylim(-1,10)
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
plt.plot(x,y)
plt.show()
