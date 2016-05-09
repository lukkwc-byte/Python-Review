from itertools import *
S, k = input().split()
k = int(k)
print(*sorted(["".join(A) for A in list(permutations(S, k))]), sep = "\n")