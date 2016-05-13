import numpy as np
N, M = [int(i) for i in input().split()]
A = np.array([input().split() for i in range(N)], int)
print(np.mean(A, axis = 1), np.var(A, axis = 0), np.std(A), sep = "\n")