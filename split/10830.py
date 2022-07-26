N, B = map(int,input().split())

A = []
for i in range(N):
    A.append(list(map(int,input().split())))
    

def matrix(a,b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    
    temp = matrix(a, b//2)
    
    ret = []
    for i in range(N):
        ret.append(calc(temp[i],temp))
        
    if b % 2 == 1:
        for i in range(N):
            ret[i] = calc(ret[i],a)
    return ret

def calc(a,b):
    temp = []
    for i in range(N):
        sum = 0
        for j in range(N):
            sum+= a[j] * b[j][i]%1000
        temp.append(sum%1000)
    return temp

res = matrix(A,B)
for i in res:
    print(*i)