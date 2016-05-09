import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(" ".join(list(map(str, list(itertools.product(A,B))))))
