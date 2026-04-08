import pandas as pd

df = pd.read_csv("python learner 5.0/data.csv")
print(df.head(2))
print(df.tail(4))
df2 =pd.read_csv("python learner 5.0/data.csv")


## drop none values but from  new copied data set

new_df = df2.dropna()
print(new_df)

#droping nan values from the original data set 

df2.dropna(inplace= True)
print(df2)
