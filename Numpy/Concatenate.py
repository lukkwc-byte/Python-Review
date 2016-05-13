import numpy
N, M, P = [int(i) for i in input().split()]
ARR1 = numpy.array([input().split() for i in range(N)], int)
ARR2 = numpy.array([input().split() for i in range(M)], int)
print(numpy.concatenate((ARR1, ARR2), axis = 0))