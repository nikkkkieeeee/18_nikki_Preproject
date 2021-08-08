import pandas as pd
data = pd.read_excel('dataNew.xls')
print(data)

data.index = data['Period']
del data['Period']
data.index

data.head(11)
data.loc[10:30]
data.tail(11)
print(data.head(11))
print(data.loc[11:19])
print(data.tail(11))

import matplotlib.pyplot as plt
ax = data[['Calories', 'Period']].plot(kind='bar', title="1900 to 1910", figsize=(10,10), legend=True, fontsize=12)
plt.show();

# import matplotlib.pyplot as plt
# plt.bar()
# plt.title('1900-1910')
# plt.xlabel('Year')
# plt.ylabel('No. of calories')
# plt.show();
