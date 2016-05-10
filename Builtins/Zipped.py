N, X = map(int, input().split())
G = list(zip(*[list(map(float, input().split())) for i in range(X)]))
for g in G:
    print(round(sum(g) / X, 2))