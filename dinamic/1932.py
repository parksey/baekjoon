N = int(input())

n_list = [[0 for _ in range(i+1)] for i in range(N)]

n_list[0][0] = int(input())

for i in range(1,N):
    line = list(map(int, input().split()))
    
    n_list[i][0] = line[0] + n_list[i-1][0]
    n_list[i][i] = line[i] + n_list[i-1][i-1]
    for j in range(1,i):
        n_list[i][j] = line[j] + (n_list[i-1][j-1] if n_list[i-1][j-1] > n_list[i-1][j] else n_list[i-1][j])
       
print(max(n_list[N-1])) 