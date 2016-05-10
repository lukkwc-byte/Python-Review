N, A = int(input()), list(map(int, input().split()))
print(all(i > 0 for i in A) and any(i == int(str(i)[::-1]) for i in A))

    
