from collections import deque

N, M = map(int ,input().split())

gMap = []
dir = [[-1,0],[0,-1],[1,0],[0,1]]

for i in range(N):
    gMap.append(list(map(int, input().split())))
      
def bfs(i,j, visitMap):
    ice = deque([[i,j]])
    newIce = deque([])
    while ice:
        left = ice.popleft()
        if visitMap[left[0]][left[1]] == 1:
            continue
        
        visitMap[left[0]][left[1]] = 1
        cnt = 0
        for d in dir:
            y = d[0] + left[0]; x = d[1]+left[1]
            
            if y >= N or y < 0 or x >= M or x < 0 or visitMap[y][x]:
                continue
            if gMap[y][x] == 0:
                cnt+=1
                continue
            
            ice.append([y,x])
        newIce.append([left[0],left[1],cnt])
            
    while newIce:
        i,j,n = newIce.popleft()
        temp = gMap[i][j] - n
        gMap[i][j] = 0 if temp <= 0 else temp 
    return 1            
    

def solve():
    year = 0
    
    while True:
        visitMap = [[0]*M for i in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(M):
                if gMap[i][j] == 0 or visitMap[i][j]==1:
                    continue
                
                cnt += bfs(i,j, visitMap)
                   
        if cnt == 0:
            return 0         
        if cnt >= 2:
            return year
        year += 1

print(solve())