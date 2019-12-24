import matplotlib.pyplot as plt
import pandas as pd

import asyncio as ac

df = pd.read_csv("ZZConstructionPoints.csv")

x = df["START_DATE"].as_matrix()  # casting SalesID to list #extracting the column with name SalesID
y = df["ID"].as_matrix()  # casting ProductPrice to list
plt.xlabel("SalesID")  # assigning X-axis label
plt.ylabel("ProductPrice")  # assigning Y-axis label
plt.title("Sales Analysis")  # assigning Title to the graph

plt.show()

ac.locks
