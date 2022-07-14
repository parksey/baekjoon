N = int(input())

n = N
arr = []
result = [0,0]

for i in range(N):
    arr.append(input().split())
    
def split(x,y, n):
    if n == 1:
        result[int(arr[y][x])] += 1
        return
    
    temp = arr[y][x]
    isAll = True
    for i in range(n):
        for j in range(n):
            if temp != arr[y+i][x+j]:
                isAll = False
                break
        if not isAll:
            break
    
    if isAll:
        result[int(temp)] += 1
        return
    
    n //= 2
    split(x,y, n)
    split(x+n, y, n)
    split(x, y+n, n)
    split(x+n, y+n, n)
    
split(0,0, n)

for r in result:
    print(r)