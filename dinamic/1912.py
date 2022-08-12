N = int(input())
n_sum = [0 for i in range(N)]

n_list = list(map(int, input().split()))

n_sum[0] = n_list[0]
result = n_sum[0]
for i in range(1,N):
    if n_sum[i-1] <0:
        n_sum[i] = n_list[i]
    else:
        n_sum[i] = n_list[i]+n_sum[i-1]
    
    if result < n_sum[i]:
        result = n_sum[i]
print(result)