# 스스로 푼 문제 X
N, K = map(int, input().split())
P = 1000000007

def fac(n):
    if n == 0 or n == 1:
        return 1
    if n==2:
        return 2
    ret = 2
    for i in range(3,n+1):
        ret = i * ret % P
    return ret


def pow(a,p):
    if p == 0:
        return 1
    elif p == 1:
        return a
    
    temp = pow(a,p//2)
    if p % 2:
        return temp * temp * a % P
      
    return temp * temp % P

print(fac(N) *pow(fac(K)*fac(N-K)%P, P-2) % P)
