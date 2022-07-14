N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    
    
result = [0,0,0]
def split(x,y,n):
    if n == 1:
        result[arr[y][x]+1] += 1
        return
    
    temp = arr[y][x]
    isB = False

    for i in range(n):
        for j in range(n):
            if temp != arr[y+i][x+j]:
                isB = True
                break
        if isB:
            break
    
    if not isB:
        result[temp+1] += 1
        return
    n //= 3
    for i in range(3):
        for j in range(3):
            split(x+j*n,y+i*n, n)
    
split(0,0,N)

for r in result:
    print(r)