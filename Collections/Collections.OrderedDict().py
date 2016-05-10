from collections import *
N, D = int(input()), OrderedDict()
for i in range(N):
    X = input().split()
    item = " ".join(X[:(len(X)-1)])
    price = int(X[len(X)-1])
    if item in D: 
        D[item] += price
    else: 
        D[item] = price

for k, v in D.items():
    print(" ".join([k, str(v)]))