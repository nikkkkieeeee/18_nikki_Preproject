import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
file = pd.read_excel('dataNew.xls')
print(file)

date = file['Period'].str.split(' ', n = 1, expand = True)
print(date)

file = file.assign(date_year=date[1])
print(file)

file.index = file['date_year']
print(file.index)

grp1 = file.iloc[:11]
print(grp1)
grp2 = file.iloc[11:21]
print(grp2)
grp3 = file.iloc[21:]
print(grp3)

grp1sum = sum(grp1['Calories'])
print(round(grp1sum, 1))
grp2sum = sum(grp2['Calories'])
print(grp2sum)
grp3sum = sum(grp3['Calories'])
print(grp3sum)

grp1mean = grp1sum / len(grp1['Calories'])
print(round(grp1mean, 2))
grp2mean = grp2sum / len(grp2['Calories'])
print(round(grp2mean, 2))
grp3mean = grp3sum / len(grp3['Calories'])
print(round(grp3mean, 2))

ps = grp1['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Year', fontsize=10)
plt.ylabel('No. of calories', fontsize=10)
plt.xticks(index, ps.index, fontsize=10)
plt.title('[1900-1910]')
plt.bar(ps.index, ps.values)
plt.show()

ps = grp2['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Year', fontsize=10)
plt.ylabel('No. of calories', fontsize=10)
plt.xticks(index, ps.index, fontsize=10)
plt.title('[1911-1920]')
plt.bar(ps.index, ps.values)
plt.show()

ps = grp3['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Year', fontsize=10)
plt.ylabel('No. of calories', fontsize=10)
plt.xticks(index, ps.index, fontsize=10)
plt.title('[1921-1930]')
plt.bar(ps.index, ps.values)
plt.show()