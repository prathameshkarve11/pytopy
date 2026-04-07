import numpy as np 

arr = np.floor(np.random.rand(100)*100)
print(arr)

print(arr.min())
print(arr.max())
print(arr.mean())
print(arr.sum())

greaterthan50 = arr[arr>50]

print(greaterthan50.size)