N = int(input())

re = [0 for i in range(N)]
count = 0
count2 = 0
def fibo():
    global N, count
    
    re[0] = 1
    re[1] = 1
    
    for i in range(2,N):
        count+=1
        re[i] = re[i-1] + re[i-2]
        
    return count

def fibo2(n):
    global count2
    if n == 1 or n==2:
        count2+=1
        return 1
    
    return fibo2(n-1) + fibo2(n-2)

fibo2(N)
print(count2, fibo())
    