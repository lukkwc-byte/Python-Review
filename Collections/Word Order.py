from collections import *
N = int(input())
D = OrderedDict()
for i in range(N):
    X = input()
    if not X in D:
        D[X] = 1
    else:
        D[X] += 1

print(len(D.keys()), " ".join([str(i) for i in D.values()]), sep = "\n")