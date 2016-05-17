import re
N = int(input())
for i in range(N):
    IN = input()
    name, email = IN.split()
    email = email[1:-1]
    if re.fullmatch('[{ALPHA}][\w\-\._]*@[{ALPHA}]*\.[{ALPHA}]{{1,3}}'.format(ALPHA = 'abcdefghijklmnopqrstuvwxyz'), email, re.I) != None: 
        print(IN)
        