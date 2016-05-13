S = input()
N = ""
for i in range(len(S)):
    if S[i].isalpha():
        if S[i].islower():
            N += S[i].upper()
        else:
            N += S[i].lower()
    else:
        N += S[i]
print(N)