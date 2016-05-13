from __future__ import division
N = input()
GRADES = {}
for i in range(N):
    STUDENT, MATH, PHYS, CHEM = raw_input().split()
    GRADES[STUDENT] = '{0:.2f}'.format(round((float(MATH) + float(PHYS) + float(CHEM)) / 3.0, 2))
    
Q = raw_input()
print(GRADES[Q])