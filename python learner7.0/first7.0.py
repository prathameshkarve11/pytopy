import pandas as pd

dataset = {
    "Names":["Raj", "Rushi", "Shivansh", "Prathamesh", "Anshuman"],
    "Age":[21,20,20,19,None]
}

# s1 = pd.Series(dataset.__sizeof__())
# print(s1)

df = pd.DataFrame(dataset)


# df.dropna(inplace= True)  
# df.fillna(45 , inplace= True)
# print(df)

print(df["Names"].min())

print(df[df["Age"] == 19])


print(df[df["Age"] == 19])


print(df[df["Age"] == 19])


print(df[df["Age"] == 19])


print(df[df["Age"] == 19])


print(df[df["Age"] == 19])


print(df[df["Age"] == 19])


print(df[df["Age"] == 19])

