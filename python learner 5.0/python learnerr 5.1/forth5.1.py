import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("python learner 5.0/data.csv")

# learning how the matplotible library works and the pyplot module works 

# plt.plot([1,42,30],[4,45,6])
# plt.show()


df.plot()
plt.show()

# this shows tjhe graph of the entire data.csv file


# kind = "scatter"

df.plot(kind="scatter", x = 'Duration', y = 'Calories')
plt.show()

# kind = 'hist'

df.plot(kind="hist", x = 'Duration', y = 'Calories')
plt.show()

