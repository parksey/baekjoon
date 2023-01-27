N, M = map(int ,input().split())
mapList = [list(map(int, input().split())) for i in range(N)]

sumList = [[0 for i in range(M+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        sumList[i][j] = mapList[i-1][j-1] + sumList[i][j-1] + sumList[i-1][j] - sumList[i-1][j-1] 


K = int(input())

def solve(x1,y1,x2,y2):
    return sumList[x2][y2] - sumList[x2][y1-1] - sumList[x1-1][y2] + sumList[x1-1][y1-1]

for i in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    print(solve(x1,y1,x2,y2))