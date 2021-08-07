import pandas as pd
data = pd.read_excel('dataNew.xls')
print(data)

data.head(11)
data.loc[10:30]
data.tail(11)
print(data.head(11))
print(data.loc[11:19])
print(data.tail(11))

import matplotlib.pyplot as plt
plt.bar()
plt.title('1900-1910')
plt.xlabel('Year')
plt.ylabel('No. of calories')
plt.show()