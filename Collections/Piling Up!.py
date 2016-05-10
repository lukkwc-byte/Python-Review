from collections import deque
T = int(input())

def Possible(D):
    S = []
    while D != []:
        if len(D) == 1:
            if S == [] or D[0] <= S[-1]:
                return "Yes"
            else:
                return "No"
        else:
            if D[0] >= D[-1] and (S == [] or D[0] <= S[-1]) :
                S.append(D.popleft())
            elif D[-1] > D[0] and (S == [] or D[-1] <= S[-1]):
                S.append(D.pop())
            else:
                return "No"

for i in range(T):
    N,D = int(input()), deque([int(i) for i in input().split()])
    print(Possible(D))



