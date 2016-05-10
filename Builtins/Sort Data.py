N, M = map(int, input().split())
L = [[int(x) for x in input().split()] for i in range(N)]
K = int(input())
O = sorted(L, key = lambda x: x[K])
for lis in O:
    print(" ".join(str(i) for i in lis))