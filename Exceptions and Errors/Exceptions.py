T = int(input())
for i in range(T):
    A, B = input().split()
    try:
        print(str(round(int(A) // int(B),0)))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
        
        