import numpy as np 

# mat1 = np.random.randint(1,50, size=(2,2))

# mat2 = np.random.randint(1,50, size=(2,2))

# matmul = np.dot(mat1,mat2)     #mat1 @ mat2
# print(matmul)
# print(mat1.T)
# det = np.linalg.det(mat1)
# print(det)



matt = np.random.rand(10,10);
print(matt)

matt [matt < 0.5] = 0
matt [matt >= 0.5] = 1
print(matt)