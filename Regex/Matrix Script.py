import re

n, m = map(int, input().split())

bytes = [''] * (n * m)
for i in range(n):
    row = input()
    for j in range(m):
        bytes[j * n + i] = row[j]

code = ''.join(bytes)
print(re.sub(r'(?<=[A-Za-z0-9])([ !@#$%&]+)(?=[A-Za-z0-9])', ' ', code))