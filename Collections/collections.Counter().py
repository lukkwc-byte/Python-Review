from collections import *
N, S, X, M = int(input()), [int(i) for i in input().split()], int(input()), 0
D = Counter(S)

for i in range(X):
    s, x = [int(i) for i in input().split()]
    if D[s] > 0:
        D[s] -= 1
        M += x

print(M)
