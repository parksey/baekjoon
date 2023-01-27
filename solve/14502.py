from collections import deque
MAX_COUNT = 3

N, M = map(int, input().split())

localMap = []
virusMap = []
direction = [[0,-1], [-1,0], [0,1], [1,0]]
wallCount = 3
mapSize = N*M
for i in range(N):
    localMap.append(list(map(int, input().split())))
    
    for j in range(M):
        if localMap[i][j] == 2:
            virusMap.append([i,j])
        elif localMap[i][j] == 1:
            wallCount += 1

maxSize = 0

def bfs():
    queue = deque(virusMap)
    checkMap = [[0 for i in range(M)] for i in range(N)]
    
    count = 0
    while queue:
        y,x = queue.popleft()
        
        if checkMap[y][x] != 0 or localMap[y][x] == 1:
            continue
        
        count += 1
        checkMap[y][x] = 1
        
        for d in direction:
            newY, newX = y + d[0], x+d[1]    
            if newY < 0 or newY >= N or newX < 0 or newX >= M:
                continue
            
            queue.append([newY,newX])
    # for d in localMap:
    #     print(*d)
    # print(mapSize - count - wallCount)
    return count

def setMap(startN, startM, deepth):
    global maxSize
    if deepth == MAX_COUNT:
        safeCount = mapSize - bfs() - wallCount
        if maxSize < safeCount:
            maxSize = safeCount
        return

    for i in range(startN, N):
        for j in range(startM, M):
            if localMap[i][j] == 0:
                localMap[i][j] = 1
                setMap(i,j+1,deepth+1) 
                localMap[i][j] = 0
        startM = 0

setMap(0,0, 0)
print(maxSize)