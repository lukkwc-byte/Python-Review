N, M = list(map(int, input().split()))
Q = list(map(int, input().split()))
A, B = set(map(int, input().split())), set(map(int, input().split()))

H = 0

for i in Q:
    if i in A: H += 1
    elif i in B: H -= 1

print(H)