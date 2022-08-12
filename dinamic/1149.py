N= int(input())

n_list = [[0,0,0] for i in range(N)]

temp = list(map(int, input().split()))
n_list[0] = temp
for i in range(1,N):
    temp = list(map(int, input().split()))
    n_list[i][0] = temp[0] + (n_list[i-1][1] if n_list[i-1][1] < n_list[i-1][2] else n_list[i-1][2])
    n_list[i][1] = temp[1] + (n_list[i-1][2] if n_list[i-1][2] < n_list[i-1][0] else n_list[i-1][0])
    n_list[i][2] = temp[2] + (n_list[i-1][0] if n_list[i-1][0] < n_list[i-1][1] else n_list[i-1][1])

print(min(n_list[N-1]))