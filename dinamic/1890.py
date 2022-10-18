from collections import deque


N = int(input())

gMap = [list(map(int ,input().split())) for __ in range(N)]

def solve():
    checkMap = [[0 for _ in range(N)] for __ in range(N)]
    checkMap[0][0] = 1
    queue = deque([[0,0]])
    
    for i in range(N):
        for j in range(N):
            dist = gMap[i][j]
            if dist == 0 or checkMap[i][j]==0:
               continue
            if i+dist < N:
                checkMap[i+dist][j] += checkMap[i][j]
            if j+dist < N:
                checkMap[i][j+dist] += checkMap[i][j] 

    return checkMap[N-1][N-1]

print(solve())