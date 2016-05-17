import re
N = int(input())
for i in range(N):
    S = input()
    if re.search('[789]\d\d\d\d\d\d\d\d\d', S, re.ASCII) != None and len(S) == 10: 
        print('YES')
    else:
        print('NO')