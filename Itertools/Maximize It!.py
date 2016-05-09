from itertools import *
K, M = list(map(int, input().split()))
L = []
I = []
T, S = 0, 0

for i in range(K):
	L.append([int(x)**2 for x in input().split()])

for x in [list(p) for p in list(product(*L))]:
	T = sum(x) % M
	if S < T: S = T

print(S)
