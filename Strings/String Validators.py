S = input()
alnum, alpha, digit, lower, upper = False, False, False, False, False
for char in S:
    if char.isalnum() == True:
        alnum = True
    if char.isalpha() == True:
        alpha = True
    if char.isdigit() == True:
        digit = True
    if char.islower() == True:
        lower = True
    if char.isupper() == True:
        upper = True
print(alnum, alpha, digit, lower, upper, sep = "\n")