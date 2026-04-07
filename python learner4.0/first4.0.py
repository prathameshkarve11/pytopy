import numpy as np

arr = np.array([3,4,5,6,7])

arr2 = np.arange(1,11,1)
print(arr2)
print(arr2.sum())
print(arr2.mean())
print(arr2.std())


arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr3.reshape(1,9)
print(arr3)


# arr4 = np.arange(1,13).reshape(4,3)
# print(arr4)

# arrrandom = np.random.rand(5,5)
# print(arrrandom)
# print(arrrandom[0])  #foirst row
# print(arrrandom[:,0]) #first colom
# print(arrrandom[:,-1]) #last colom
# print(arrrandom[-1]) #last row
# print(arrrandom[2,2]) ### midle element



### 1,m23

arr120 = np.arange(1,21,1)
for i in range(0,20):
    if(arr120[i]%2 == 0):
        print(arr120[i])

for x in arr120:
    if(x %2 == 0):
        print(x)

even = arr120[arr120%2 == 0]
print(even)


grt10 = arr120[arr120 > 10]
print(grt10)



### arra add multiply


a1 = np.arange(1,4)
a2 = np.arange(10,40,10)

sumar = a1 + a2
mult = a1*a2

print( a1 )
print(a2)
print(f"sum is  { sumar}")
print(f"multiply is {mult}")
