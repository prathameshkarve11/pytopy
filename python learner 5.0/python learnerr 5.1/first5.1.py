import pandas as pd
# creatig a data frame 

df = pd.DataFrame([4,5,6,7,8,9] ,columns=["points"])
print(df.to_string())

# creating a data  dictornary 

data  = {
    "Name": ["raj", "rushi", "kayak"],
    "age": [34,5,6]
}

df2 = pd.DataFrame(data)
print(df2)
print(type(df2))
print(df2.head())


### pandas series  

a = ["pter", "gter", "mter"]
print(pd.Series(a))


# dataframe is a collection of series 
# series is 1 dimetionsal ; 1 colom only 
# dataframe is multidimetaional , multiple coulmsa or seires 

print(pd.Series(data))  # this gives the data as one array in one column 

