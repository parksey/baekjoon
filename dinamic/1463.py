N = int(input())
n_list = [0 for i in range(N+1)]

for i in range(2,N+1):
    i3 =1000000
    i2 =1000000
    i1 =1000000
    if i%3==0:
        i3 = n_list[i//3]+1
    if i%2==0:
        i2 = n_list[i//2]+1
    i1 = n_list[i-1]+1
    n_list[i] = min(i1,i2,i3)
print(n_list[N])
        
    