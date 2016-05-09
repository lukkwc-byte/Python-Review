from itertools import *
N, L, K = int(input()), input().split(), int(input())
C = [set(A) for A in list((combinations(L, K)))]
O = 0
for S in C:
	if "a" in S: O += 1
print(O/len(C))