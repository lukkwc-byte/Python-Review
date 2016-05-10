from collections import *
N, Student = int(input()), namedtuple('Student', ",".join(input().split()))
print(round(sum([int(y) for y in [Student(*input().strip().split()).MARKS for i in range(N)]]) / N, 2))
