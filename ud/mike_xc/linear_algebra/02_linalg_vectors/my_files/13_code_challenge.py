import numpy as np

# print('hi!')

# print('hi again!')

matA = np.random.randint(-2,4,size=(4,6))
matB = np.random.randint(-2,5,size=(4,6))

print(matA) 
print(matB)


# print(matB
#.shape[1])

# for i in range(matA.shape[0]):
#     coltotal = 0
#     for j in range(matA.shape[1]):
#         coltotal += matA[i][j] * matB[i][j]
    # print(coltotal)
    

print("Looping:\n")

for j in range(matA.shape[1]):
    coltotal = 0
    for i in range(matA.shape[0]):
        coltotal += matA[i][j] * matB[i][j]
    print(coltotal)

print('\nnp.dot\n')

for j in range(matA.shape[1]):
    print(np.dot(matA[:,j], matB[:,j]))

