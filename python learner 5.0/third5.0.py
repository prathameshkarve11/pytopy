import pandas as pd

df = pd.read_json('python learner 5.0/data.json')
pd.options.display.max_rows = 9999
print(df.to_string())
print(df.head(10))
print(df.tail(4))
print(df.info()) 