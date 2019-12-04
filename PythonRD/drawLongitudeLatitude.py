import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("testData.csv")
print (data.head(10))

plt.scatter(x=data['Longitude'], y=data['Latitude'])
plt.show()

data2 = pd.read_csv("testData.xlsx")
plt.scatter(x=data2['Longitude'], y=data2['Latitude'])
plt.show()
