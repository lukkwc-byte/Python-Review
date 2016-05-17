import string
import re
T = int(input())
for i in range(T):
	S = input()
	if (
        re.fullmatch('[\w]*', S, re.I) != None and 
        len([match.group() for match in re.finditer('\d', S, re.ASCII)]) >= 3 and 
        len([match.group() for match in re.finditer('[{valid}]'.format(valid = string.ascii_uppercase), S, re.ASCII)]) >= 2 and 
        len(S) == 10 and 
        len(set(S)) == len(S)):
			print('Valid')
	else:
		print('Invalid')