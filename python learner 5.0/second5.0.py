import pandas as pd

df = pd.read_csv('python learner 5.0/data.csv')
pd.options.display.max_rows = 9999
print(df.to_string)
print(pd.options.display.max_rows)