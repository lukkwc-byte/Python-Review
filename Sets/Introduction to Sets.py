N = int(input())
L = map(int, input().split())
D = set(L)
print(sum(list(D))/len(list(D)))