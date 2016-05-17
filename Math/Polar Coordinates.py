import cmath
import math

eq = raw_input()
pa = cmath.phase(complex(eq))
r = abs(complex(eq))

print ("{0}\n{1}".format(r,pa))