import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("testData.csv")
print (data.head(10))

plt.scatter(x=data['Longitude'], y=data['Latitude'])
plt.show()

