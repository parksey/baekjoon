N, M = map(int, input().split())

candyMap = [list(map(int, input().split())) for i in range(N)]

def solve():
    maxMap = [[0 for __ in range(M)] for _ in range(N)]
    
    maxMap[0][0] = candyMap[0][0]
    
    for n in range(1, N):
        maxMap[n][0] = candyMap[n][0] + maxMap[n-1][0]
        
    for m in range(1,M):
        maxMap[0][m] = candyMap[0][m] + maxMap[0][m-1]
    
    for n in range(1, N):
        for m in range(1, M):
            maxMap[n][m] = candyMap[n][m] + max(maxMap[n][m-1], maxMap[n-1][m], maxMap[n-1][m-1])
    
    return maxMap[N-1][M-1]
print(solve())