import numpy as np

vA = np.random.randn(100)
vB = np.random.randn(100)

vC = np.random.randint(1, 10, size=2)
vD = np.random.randint(1, 10, size=2)

print(vA) 
# print(vB)

# print(np.dot(vA[:,0], vB[:,0]))
print(np.dot(vA, vB))
print(np.dot(vB, vA))
# print(np.dot(vB[:,0], vA[:,0]))

print(vC)
print(vD)

print(np.dot(vC, vD))

print(np.dot(vD, vC))
    

# print("Looping:\n")

# for j in range(vA.shape[1]):
#     coltotal = 0
#     for i in range(vA.shape[0]):
#         coltotal += vA[i][j] * vB[i][j]
#     print(coltotal)

# print('\nnp.dot\n')

# for j in range(vA.shape[1]):
#     print(np.dot(vA[:,j], vB[:,j]))



