# Data exploration flow

import matplotlib.pyplot as plt
import pandas as pd

# Loading data set
data = pd.read_csv("data.csv")

# Loading information for the given dataset
fig, ax = plt.subplots()

ax.plot(
    data["Month"], data["Rainfall_mm"], label="Trend line", color="blue", linewidth=2
)

ax.set_title("Rain fall analysis")
ax.set_xlabel("Rain fall count")
ax.set_ylabel("Months")
plt.show()
