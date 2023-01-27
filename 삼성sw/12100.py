from collections import deque
import sys
import copy
N = int(input())

MAX_COUNT = 5
gMap = []
for i in range(N):
    gMap.append(list(map(int, input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def merge(tMap, dy, dx):
    if dy == 0:
        originX = 0 if dx == 1 else N-1
        # each line
        for i in range(N):
            x = originX
            # 시작
            while True:
                while (x >= 0 and x < N) and tMap[i][x] == 0:
                    x += dx
                newX = x+dx
                while (newX >= 0 and newX < N) and tMap[i][newX] == 0:
                    newX += dx

                if newX >= N or newX < 0:
                    break
                
                if tMap[i][x] == tMap[i][newX]: 
                    tMap[i][x] *= 2
                    tMap[i][newX] = 0
                    x = newX+dx
                else:
                    x = newX
        
            # 밀어주기
            x = originX
            startIndex = originX

            while x >= 0 and x < N:
                if tMap[i][x] != 0:
                    data = tMap[i][x] 
                    tMap[i][x] = 0
                    tMap[i][startIndex] = data
                    startIndex += dx 
                x += dx
        
    elif dx == 0:
        originY = 0 if dy == 1 else N-1
        
        # each line
        for i in range(N):
            y = originY

            # 시작
            while True:
                while (y >= 0 and y < N) and tMap[y][i] == 0:
                    y += dy
                newY = y+dy
                while (newY >= 0 and newY < N) and tMap[newY][i] == 0:
                    newY += dy
                
                if newY >= N or newY < 0:
                    break
                
                
                if tMap[y][i] == tMap[newY][i]: 
                    tMap[y][i] *= 2
                    tMap[newY][i] = 0
                    y = newY+dy
                else:
                    y = newY
            
            y = originY
            startIndex = originY
            while y >= 0 and y < N:
                if tMap[y][i] != 0:
                    data = tMap[y][i] 
                    tMap[y][i] = 0
                    tMap[startIndex][i] = data
                    startIndex += dy 
                y += dy

def find(tMap):
    retMax =0 
    for i in range(N):
        retMax = max(max(tMap[i]), retMax)
    return retMax 

def printMap(tMap):
    for i in range(N):
        print(tMap[i])

def solve():
    
    queue = deque([[copy.deepcopy(gMap), 0]])
    result = 0
    result = max(result, find(gMap))
    while queue:
        curMap, cnt = queue.popleft()

        if cnt >= MAX_COUNT:
            break
        
        for d in range(len(dx)):
            tempMap = copy.deepcopy(curMap)

            merge(tempMap, dy[d], dx[d])
            result = max(result, find(tempMap))
            queue.append([copy.deepcopy(tempMap), cnt+1])
    return result
print(solve())