a = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    Q = input().split()
    C = Q[0]
    if C == "intersection_update":
        A &= set(map(int, input().split()))
    elif C == "update":
        A |= set(map(int, input().split()))
    elif C == "symmetric_difference_update":
        A ^= set(map(int, input().split()))
    elif C == "difference_update":
        A -= set(map(int, input().split()))
    else:
        print("error")
print(sum(list(A)))