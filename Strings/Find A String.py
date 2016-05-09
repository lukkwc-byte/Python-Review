O, S = input(), input()
W = len(S)
C = 0
for i in range(len(O)):
    if O[i : i + W] == S:
        C += 1
print(C)