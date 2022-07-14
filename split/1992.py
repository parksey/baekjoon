N = int(input())
n= N

arr = []

for i in range(N):
    arr.append(input())
  
result = ""
def split(x,y,n):
    global result
    if n==1:
        result += arr[y][x]
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
        result += temp
        return
    
    result += "("
    n//=2
    split(x,y,n)
    split(x+n,y,n)
    split(x,y+n,n)
    split(x+n,y+n,n)
    result += ")"
    
split(0,0,n)
print(result)