N = int(input())
K = int(input())

k_map = [[i*j for j in range(1,N+1)] for i in range(1,N+1)]

index = 1
cnt = 1
for i in range(1,N+1):
    if cnt +(i+1) >= K:
        index = i
        break
    cnt += (i+1)
    
if index == 1:
    index = N
    
if index%2==0:
    