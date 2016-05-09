from itertools import *
S = input()

print(*(list(map(str, [(len(list(g)), int(k)) for k, g in groupby(S)]))))