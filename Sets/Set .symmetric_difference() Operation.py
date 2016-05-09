n, E = int(input()), set(map(int, input().split()))
b, F = int(input()), set(map(int, input().split()))
print(len(list(E ^ F)))