from collections import *
def Valid(S):
	D = Counter(S)
	
	if not (("@" in D and D["@"] == 1) and ("." in D and D["."] == 1)): return False
	
	s1 = S.index("@")
	s2 = S.index(".")
	usr = S[:s1]
	web = S[s1+1:s2]
	ext = S[s2+1:]
	
	if len(ext) > 3 or len(usr) < 1: return False
	
	if not web.isalnum(): return False

	if not all([str.isalnum(s) or s == "-" or s == "_" for s in usr]): return False

	return True

N = int(input())
V =[]
for i in range(N):
	S = input()
	if Valid(S) == True: 
		V.append(S)

print(sorted(V))