N = int(input())
f = [0, 1, 1]
F = f[:N] 
if N > 3:
    for i in range(2, N-1):
        F.append(F[i]+F[i-1])
print(list(map(lambda x: x**3, F)))