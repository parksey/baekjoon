T = int(input())

def mul(d1, d2):
    ret = 0
    for i in range(len(d1)):
        ret += d1[i] * d2[i]
    return ret 
    

def solve():
    N, M= map(int, input().split())
    nList = list(map(int, input().split()))
    mList = list(map(int, input().split()))
    
    bigList= nList
    smallList = mList
    bigNum = N
    smallNum = M
    if N < M:
        bigList, smallList = mList, nList
        bigNum, smallNum = M, N
        
    ret = mul(smallList, bigList[:smallNum])
    
    for i in range(1, bigNum-smallNum+1):
        calc = mul(smallList, bigList[i:smallNum+i])
        print(calc)
        if ret < calc:
            ret = calc
    return ret

for i in range(T):
    print("#{} {}".format(i+1, solve()))