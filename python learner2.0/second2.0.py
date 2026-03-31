import numpy as np
### written this com from github to fetch this in envirment
## numpy installled 

### first array with numpy
arr = np.array([2,4,6,7,8])
print(arr)
print(arr[0])

# directly adding subtracting multiplying to all elements at onecce 

print(arr + 1)
print(arr - 1)
print(arr * 2)

### print mean of array 
print(np.mean(arr))
print(np.sum(arr))


### 2d and 3d  arrays in numpy 

mat2d = np.array([[2,4], [5,7]])
print(mat2d)
print(mat2d.shape)

mat3d = np.array([[2,4],[4,8],[4,3]])
print(mat3d)
print(mat3d.shape)


### create array 1 to 10 , min max mean , mulitply all by 5

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(F"mean: {np.mean(a)} and the min value is : {np.min(a)}, and max value is {np.max(a)}")
