import pandas as pd
data = pd.read_excel('dataNew.xls')
print(data)

datas = data['Period'].str.split(' ', n = 1, expand = True)
print(datas)

data = data.assign(year=datas[1])

data.index = data['year']
del data['year']
print(data.index)

set1 = data.head(11)
print(set1)

set2 = data.iloc[11:21]
print(set2)

set3 = data.tail(10)
print(set3)

import numpy as np
import matplotlib.pyplot as plt

ps = set1['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=15)
plt.ylabel("No. of calories", fontsize=15)
plt.xticks(index, ps.index, fontsize=15)
plt.title("[1900-1910]", size=18)
plt.show();

ps = set2['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=15)
plt.ylabel("No. of calories", fontsize=15)
plt.xticks(index, ps.index, fontsize=15)
plt.title("[1911 to 1920]", size=18)
plt.show();

ps = set3['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=15)
plt.ylabel("No. of calories", fontsize=15)
plt.xticks(index, ps.index, fontsize=15)
plt.title("[1921 to 1930]", size=18)
plt.show();

set3.mean()

