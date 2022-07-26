N_A, M_A = map(int, input().split())

A = []
for i in range(N_A):
    A.append(list(map(int,input().split())))
    
N_B, M_B = map(int, input().split())
B = []
for i in range(N_B):
    B.append(list(map(int,input().split())))
    
def matrix(A,B):
    temp = []
    for i in range(M_B):
        sum = 0
        for j in range(M_A):
            sum+= A[j] * B[j][i]
        temp.append(sum)
    return temp

result = []
for i in range(N_A):
    print(' '.join(list(map(str, matrix(A[i],B)))))