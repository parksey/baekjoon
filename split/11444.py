N = int(input())

A = [
    [1,1],
    [1,0]
]
mod = 1000000007

def fibo(n,a):
    if n==1:
        for i in range(2):
            for j in range(2):
                a[i][j] %= mod
        return a
    
    temp = fibo(n//2, a)
    
    ret =[]
    for i in range(2):
        ret.append(calc(temp[i],temp))

    if n % 2:
        for i in range(2):
            ret[i] = calc(ret[i], a)
    return ret    
    
def calc(A,B):
    temp = []
    for i in range(len(A)):
        sum = 0
        for j in range(len(B)):
            sum += A[j] * B[j][i] % mod
        temp.append(sum%mod)
    return temp
    
result = fibo(N,A) 
print(result[1][0])