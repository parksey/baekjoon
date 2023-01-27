T = int(input())

def solve():
    N = int(input())
    
    ret = ""
    
    for i in range(N):
        c, num = input().split()        
        ret += c*int(num)
        
    length = len(ret)
    
    n = length // 10
    
    for i in range(n):
        print(ret[i*10:10*(i+1)])
    print(ret[n*10:])
    
    
for i in range(T):
    print("#{}".format(i+1))
    solve()