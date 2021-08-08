import pandas as pd
data = pd.read_excel('dataNew.xls')
print(data)

data.index = data['Period']
del data['Period']
data.index

grp1 = data.head(11)
print(grp1)

# data.iloc[11:20]
# print(data.iloc[11:20])
#
# data.tail(11)
# print(data.tail(11))

import numpy as np
import matplotlib.pyplot as plt
data = grp1['Calories'].plot(kind='bar', title="1900-1910", figsize=(10,10), legend=True, fontsize=10)
plt.show();
# ps = grp1['Calories'].sorted_values()
# index = np.arange(len(ps.index))
# plt.bar(ps.index, ps.values)
# plt.xlabel("Year", fontsize=15)
# plt.ylabel("No. of calories", fontsize=15)
# plt.xticks(index, ps.index, fontsize=15)
# plt.title("[1900-1910]", size=18)
# plt.show()

