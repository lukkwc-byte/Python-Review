from itertools import *
S, k = input().split()
k = int(k)
for i in range(1, k+1):
    print(*("".join(A) for A in list(combinations(sorted(S), i))), sep = "\n")