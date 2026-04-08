### loading and using json files 
import pandas as pd

df = pd.read_json("python learner 5.0/data.json")

print(df.head())
print(df.tail())
print(df.duplicated())
df.drop_duplicates(inplace= True)

print(df.corr())