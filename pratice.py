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

set1sum = sum(set1['Calories'])
print(round(set1sum))
set2sum = sum(set2['Calories'])
print(round(set2sum))
set3sum = sum(set3['Calories'])
print(round(set3sum))

set1mean = set1sum / len(set1['Calories'])
print(round(set1mean, 2))
set2mean = set1sum / len(set2['Calories'])
print(round(set2mean, 2))
set3mean = set3sum / len(set3['Calories'])
print(round(set3mean, 2))

import numpy as np
import matplotlib.pyplot as plt

ps = set1['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=10)
plt.ylabel("No. of calories", fontsize=10)
plt.xticks(index, ps.index, fontsize=10)
plt.title("[1900-1910]", size=12)
plt.show();

ps = set2['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=10)
plt.ylabel("No. of calories", fontsize=10)
plt.xticks(index, ps.index, fontsize=10)
plt.title("[1911 to 1920]", size=12)
plt.show();

ps = set3['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=10)
plt.ylabel("No. of calories", fontsize=10)
plt.xticks(index, ps.index, fontsize=10)
plt.title("[1921 to 1930]", size=12)
plt.show();

