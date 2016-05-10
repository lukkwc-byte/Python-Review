from collections import *
N, M = list(map(int, input().split()))
A = defaultdict(list)
for i in range(1, N+1):
	x = input()
	if not(x in A):
		A[x] = [i]
	else:
		A[x].append(i)

for i in range(M):
	x = input()
	if not(x in A): print(-1)
	else: print(" ".join(str(y) for y in A[x]))
