def Wrapper(func):
	def Standardizer(A):
		A = [str(int(S)) for S in A]
		ret = list(map(lambda x: x[2:] if len(x) == 12 else x, A))
		A = sorted(ret)
		return func(A)
	return Standardizer

@Wrapper
def Format(A):
	return ["+91 " + i[:5] + " " + i[5:] for i in A]

N = int(input())
A = [input() for i in range(N)]
R = Format(A)
print("\n".join(R))
	-