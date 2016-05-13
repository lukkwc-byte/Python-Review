import numpy
N, M = [int(i) for i in input().split()]
IN = numpy.array([input().split() for i in range(N)], int)
print(numpy.transpose(IN), IN.flatten(), sep = "\n")