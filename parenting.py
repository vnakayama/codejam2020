from sys import stdin
import numpy as np 

T = int(stdin.readline().strip()) # número de testes
R = list()
for t in range(1,T+1):

	R.append([])
	N = int(stdin.readline().strip()) # número de atividades até 100
	P = list()
	I = list()

	for n in range(0,N):

		i = [int(s) for s in stdin.readline().split(" ")] # intervalo da atividade
		I.append(list(range(i[0],i[1]+1)))

	try:

		try:

			C = list(range(0,1141))
			J = list(range(0,1141))

			for n in range(0,N):

				try:

					for i in range(len(I[n])):
						if i == 0 and I[n][i]+1 in C:
							pass 
						else:
							C.remove(I[n][i])
					P.append('C')

				except ValueError:

					for i in range(len(I[n])):
						if i == 0 and I[n][i]+1 in J:
							pass 
						else:
							J.remove(I[n][i])
					P.append('J')

		except ValueError:

			C = list(range(0,1141))
			J = list(range(0,1141))

			for n in range(0,N):

				try:

					for i in range(len(I[n])):
						if i == 0 and I[n][i]+1 in J:
							pass 
						else:
							J.remove(I[n][i])
					P.append('J')

				except ValueError:

					for i in range(len(I[n])):
						if i == 0 and I[n][i]+1 in C:
							pass
						else:
							C.remove(I[n][i])
					P.append('C')

	except:
		if len(P) >= N:
			pass
		else:
			P.clear()
			P.append('IMPOSSIBLE')

	R[t-1].append(t)
	R[t-1].append(''.join(P))
			
for i in range(len(R)):
    print("Case #{0}: {1}".format(R[i][0], R[i][1]))