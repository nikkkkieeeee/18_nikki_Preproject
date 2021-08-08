import pandas as pd
data = pd.read_excel('dataNew.xls')
print(data)

data = data['Period'].str.split(' ', n = 1, expand = True)
print()

set1 = set.assign(grp1date_year=set1date[1])
print(set1)

set1.index = grp1['Period']
print(set1.index)

set1 = data.head(11)
print(data.head(11))

data.iloc[11:20]
print(data.iloc[11:20])

data.tail(11)
print(data.tail(11))

import numpy as np
import matplotlib.pyplot as plt
ps = data['Calories'].sorted_values()
index = np.arange(len(ps.index))
plt.bar(ps.index, ps.values)
plt.xlabel("Year", fontsize=15)
plt.ylabel("No. of calories", fontsize=15)
plt.xticks(index, ps.index, fontsize=15)
plt.title("[1900-1910]", size=18)
plt.show()

