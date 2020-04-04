"""
Input: número de testes, N da matriz, a matriz
Output: Case #x: k r c
x número do teste
k traço
r linhas com repetição
c colunas com repetição
"""



for t in range(1,T+1):
	k = 0
	r = 0
	c = 0
	for n in range(1,N+1):
		for m in range(1,N+1):
			if len(M[m]) != len(set(M[m])):
				r = r +1
			k = k + M[m-1]
	print('Case #{}: {} {} {}'.format(t,k,r,c))