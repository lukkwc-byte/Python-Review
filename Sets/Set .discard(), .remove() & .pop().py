n = int(input())
s = set(map(int, input().split())) 
N = int(input())

for i in range(N):
    Q = input().split()
    C = Q[0]
    if C == "pop":
        s.pop()
    elif C == "discard":
        s.discard(int(Q[1]))
    elif C == "remove":
        s.remove(int(Q[1]))
    else:
        print("error")
print(sum(list(s)))