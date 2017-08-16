from matplotlib import pyplot as plt


years = [1950 + i for i in range(7)]
gdp = [300.2, 543.2, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# x축에 연도, y축에 gdp인 선그래프
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# 제목 추가
plt.title("Nominal GDP")

# y축에 라벨 추가
plt.ylabel("Billions of $")
plt.show()
