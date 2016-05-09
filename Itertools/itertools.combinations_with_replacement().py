from itertools import *
S, k = input().split()
k = int(k)
print(*("".join(A) for A in list(combinations_with_replacement(sorted(S), k))), sep = "\n")