import numpy as np
N, M  = [int(i) for i in input().split()]
A = np.array([input().split() for i in range(N)], int)
print(np.product(np.sum(A, axis = 0)))
