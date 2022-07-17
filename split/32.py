N, K = map(int, input().split())

arr = []
for i in range(N+1):
    arr.append([])
    for j in range(i+1):
        arr[i].append(0)

def split(n, k):
    if arr[n-1][k-1] != 0:
        return arr[n-1][k-1]
    
    if k == n or k == 0:
        arr[n-1][k-1] = 1
        return 1
    
    if n % 2 == 0:
        
    # arr[n-1][k-1] = split(n-1, k) + split(n-1, k-1)
    return arr[n-1][k-1]

print(split(N, K))