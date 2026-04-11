import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


df = pd.read_csv("python learner 6.0/box_office_dataset.csv")

df.plot("year", "worldwide_lifetime_gross" ,color='red', linestyle='--', marker='x')

plt.title("the whole graph")
plt.xlabel("Year")
plt.ylabel("worldwide_lifetime_gross")
plt.show()
