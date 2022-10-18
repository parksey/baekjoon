from collections import deque
from tabnanny import check


N, M = map(int, input().split())

gMap = [list(map(int, input().split())) for _ in range(N)]

def solve():
    checkMap = [[0 for _ in range(M)] for __ in range(N)]
    checkMap[0][0] = 1
    dir = [[0,-1], [-1,0], [0,1], [1,0]]
    
    stack = [[0,0]]
    cnt = 0
    while stack:
        top = stack.pop()
        
        if top[0] == N and top[1] == M:
            continue
        
        for d in dir:
            y = d[0]+top[0]; x=d[1]+top[1]
            
            if y >=N or y<0 or x>=M or x<0:
                continue
            
            if gMap[y][x] < gMap[top[0]][top[1]]:
                stack.append([y,x])
                checkMap[y][x] = 1
                
    for i in range(N):
        print(*checkMap[i])
    return checkMap[N-1][M-1]

print(solve())