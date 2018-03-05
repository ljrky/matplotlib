import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('..\datas\california_housing_train.csv')

# # 把位置信息根据散点图表示出来
# longitude = data.longitude
# latitude = data.latitude
# # 设置散点图的点的大小，点的颜色和点的透明度
# plt.scatter(longitude,latitude,s=75,alpha=0.5)
# # 设置坐标系范围和去掉刻度的值
# plt.xticks()
# plt.yticks()
# plt.show()

median_income = data.median_income
median_income_describe = median_income.describe()
median_house_value = data.median_house_value
median_house_value_describe = median_house_value.describe()

x = median_house_value_describe.index
y = median_house_value_describe.values
plt.bar(x,y)
plt.show()