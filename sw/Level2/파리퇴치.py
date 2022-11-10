T = int(input())

def solve():
    N, M = map(int, input().split())

    nList = []

    for i in range(N):
        nList.append(list(map(int, input().split())))

    size = N-M+1
    sumList = [[0]*size for i in range(size)]
    ret = 0
    for i in range(size):
        sumList[0][i] = sum([sum(nList[j][i:i+M]) for j in range(M) ])
        if ret < sumList[0][i]:
            ret = sumList[0][i]
        
    for i in range(1,size):
        for j in range(size):
            sumList[i][j] = sumList[i-1][j] - sum(nList[i-1][j:j+M]) + sum(nList[i+M-1][j:j+M])
            if ret < sumList[i][j]:
                ret = sumList[i][j]

    return ret 
    
for i in range(T):
    print("#{} {}".format(i+1, solve()))