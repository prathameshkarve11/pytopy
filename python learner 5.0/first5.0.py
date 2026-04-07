import pandas as pd

# dataset= {
#     "cars": ["bmw", "merc benz", "lambo"],
#     "passings": [4,5,7]
# }

# var = pd.DataFrame(dataset)
# print(var)



#### pandas series 

a = [23,45,5,3,2]

aser = pd.Series(a , index=["x","y", "z","e","g"])
print(aser["y"])
print(aser)