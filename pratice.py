import pandas as pd
data = pd.read_excel('dataNew.xls')
print(data)

datas = data['Period'].str.split(' ', n = 1, expand = True)
print(datas)

data = data.assign(year=datas[1])

data.index = data['year']

print(data.index)

set1 = data[(data['year'] >= str(1900)) & (data['year'] <= str(1910))]
print(set1)

set2 = data[(data['year'] >= str(1911)) & (data['year'] <= str(1920))]
print(set2)

set3 = data[(data['year'] >= str(1921)) & (data['year'] <= str(1930))]
print(set2)

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
plt.title("[1911-1920]", size=12)
plt.show();

ps = set3['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=10)
plt.ylabel("No. of calories", fontsize=10)
plt.xticks(index, ps.index, fontsize=10)
plt.title("[1921-1930]", size=12)
plt.show();

set3.mean()

class TestMarks:
    def totalset1(num):
        return sum(num)
    def meanset1(num):
        return sum(num) / len(num)

    def totalset2(num):
        return sum(num)
    def meanset2(num):
        return sum(num) / len(num)

    def totalset3(num):
        return sum(num)
    def meanset3(num):
        return sum(num) / len(num)

print(round(TestMarks.totalset1(set1['Calories']), 1))
print(round(TestMarks.totalset2(set2['Calories']), 1))
print(round(TestMarks.totalset3(set3['Calories']), 1))

print(round(TestMarks.meanset1(set1['Calories']), 1))
print(round(TestMarks.meanset2(set2['Calories']), 1))
print(round(TestMarks.meanset3(set3['Calories']), 1))