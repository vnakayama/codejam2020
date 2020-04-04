from sys import stdin
import numpy as np 

t = int(stdin.readline().strip())
result_list = []
for case in range(1,t+1):
    result_list.append([])
    n = int(stdin.readline().strip())
    r_rows = 0
    r_columns = 0
    row = []
    matrix = []
    for i in range(1,n+1):  #Catching the input
        row=[int(s) for s in stdin.readline().split(" ")] 
        matrix.append(row)

    for j in range(n):
        matrix = np.asarray(matrix)
        if (len(matrix[j]) != len(set(matrix[j]))):
                r_rows += 1 

    t_matrix = matrix.T   #Transposing the matrix

    for j in range(n):

        if (len(t_matrix[j]) != len(set(t_matrix[j]))):
                r_columns += 1 

    trace = matrix.trace() 
    result_list[case-1].append(case)
    result_list[case-1].append(trace)
    result_list[case-1].append(r_rows)
    result_list[case-1].append(r_columns)   
      
for index in range(len(result_list)):
    print("Case #{0}: {1} {2} {3}".format(result_list[index][0], result_list[index][1], result_list[index][2], result_list[index][3]))
