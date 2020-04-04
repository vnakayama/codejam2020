from sys import stdin
import numpy as np 

T = int(stdin.readline().strip())
R = list()
for t in range(1,T+1):

	R.append([])
	S = stdin.readline().strip()
	new_S = ''

	if int(S) == 0:
		R[t-1].append(t)
		R[t-1].append(S)

	for s in range(len(S)):
		if len(S) == 1:
			new_S+=int(S[s])*'('+S[s]+int(S[s])*')'
		else: 
			if s == 0:
				new_S+=int(S[s])*'('+S[s]

			if S[s] < S[s-1] and s != 0 and s != len(S)-1:
				new_S+=(int(S[s-1])-int(S[s]))*')'+S[s]
			if S[s] == S[s-1] and s != 0 and s != len(S)-1:
				new_S+=S[s]
			if S[s] > S[s-1] and s != 0 and s != len(S)-1:
				new_S+=(int(S[s])-int(S[s-1]))*'('+S[s]

			if S[s] < S[s-1] and s != 0 and s == len(S)-1:
				new_S+=(int(S[s-1])-int(S[s]))*')'+S[s]+int(S[s])*')'
			if S[s] == S[s-1] and s != 0 and s == len(S)-1:
				new_S+=S[s]+int(S[s])*')'
			if S[s] > S[s-1] and s != 0 and s == len(S)-1:
				new_S+=(int(S[s])-int(S[s-1]))*'('+S[s]+int(S[s])*')'


	R[t-1].append(t)
	R[t-1].append(new_S)
			
for i in range(len(R)):
    print("Case #{0}: {1}".format(R[i][0], R[i][1]))