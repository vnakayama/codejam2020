from sys import stdin
import numpy as np 

T = int(stdin.readline().strip()) # número de testes
R = list()
for t in range(1,T+1):

	R.append([])
	N = int(stdin.readline().strip()) # número de atividades até 100
	I = list()
	P = list()

	for n in range(1,N+1):

		i = [int(s) for s in stdin.readline().split(" ")] # intervalo da atividade
		I.append(range(i[0],i[1]+1))

	for n in range(0,N):
		if n != 0:
			if len(set(list(I[n][:]).append(I[n-1][:]))) == len(list(I[n][:]).append(I[n-1][:])):
				P.append(P[n-1])
			if len(set(list(I[n][:]).append(I[n-1][:]))) != len(list(I[n][:]).append(I[n-1][:])):	
				if P[n-1] == 'C':
					P.append('J')
				if P[n-1] == 'J':
					P.append('C')

	R[t-1].append(t)
	R[t-1].append(' '.join(P))
			
for i in range(len(R)):
    print("Case #{0}: {1}".format(R[i][0], R[i][1]))