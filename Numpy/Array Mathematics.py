import numpy as np
N, M = [int(i) for i in input().split()]
A = np.array([input().split() for i in range(N)], int)
B = np.array([input().split() for i in range(N)], int)
print(np.add(A,B), np.subtract(A,B), np.multiply(A,B), np.array(np.divide(A,B), int), np.mod(A,B), np.power(A,B), sep = "\n")