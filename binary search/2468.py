from collections import deque

N = int(input())
gMap = [list(map(int, input().split())) for i in range(N)]

def find(rain, start, checkMap):
    if gMap[start[0]][start[1]] <= rain:
        checkMap[start[0]][start[1]] = 1
        return 0
        
    queue = deque([start])
    while queue:
        y,x = queue.popleft()
        
        if checkMap[y][x] == 1:
            continue
        checkMap[y][x] = 1
        if gMap[y][x] <= rain:
            continue    
        
        if y+1 < N:
            queue.append([y+1,x])
        if x+1 < N:
            queue.append([y,x+1])
        if y-1 >= 0:
            queue.append([y-1,x])
        if x-1 >= 0:
            queue.append([y,x-1])
    return 1 
            
def solve():
    rain = 0
    maxPart = 0
    while rain<=100:
        checkMap = [[0]*N for i in range(N)]
        part = 0
        for i in range(N):
            for j in range(N):
                if checkMap[i][j] != 0:
                    continue
                part += find(rain, [i,j], checkMap)
        if maxPart < part:
            maxPart = part
        rain+=1
 
    return maxPart
print(solve())
