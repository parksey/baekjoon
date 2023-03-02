'''
R행 C열
. = 비어있는 곳
* = 물
x = 돌
D = 비버 굴
S = 고슴도치의 위치

1. 매 분마다 고슴도치는 인접 네 칸중 하나로 이동 가능
2. 물도 매분 비어있는 칸으로 확장, 비어있는 칸에만 물이 찬다.
3. 물과 고슴도치는 돌을 통과할 수 없다.
4. 고슴도치는 물의 지역을 이동 불가
5. 물도 비버의 소굴로 이동 불가
'''
from collections import deque
R, C = map(int ,input().split())

dataMap = []
endPoint = []
startPoint = []

waterMap = []
waterList = []

direction = [[-1,0], [0,-1], [1,0], [0,1]]

for i in range(R):
    data = list(input())
    waterMap.append(data.copy())
    for j in range(C):
        if data[j] == 'D':
            endPoint = [i,j] 
        elif data[j] == 'S':
            startPoint = [i,j]
        elif data[j] == "*":
            waterList.append([i,j])
    dataMap.append(','.join(data))
dataMap = ','.join(dataMap)

def isOutOfRange(y,x):
    if y>=R or y < 0 or x >=C or x< 0:
        return True
    return False

def makeWater(waterMap, waterList):
    newWaterList= [] 
    newMap= [water for water in waterMap]
    queue = deque(waterList)

    while queue:
        water = queue.popleft()
        for dir in direction:
            new_y = water[0] + dir[0]; new_x = water[1] + dir[1]
            if isOutOfRange(new_y, new_x):
                continue
            
            if newMap[new_y][new_x] == '*' \
                or newMap[new_y][new_x] == 'X' \
                or newMap[new_y][new_x] == 'D':
                continue
            
            newMap[new_y][new_x] = '*'         
            newWaterList.append([new_y, new_x])

    return [newMap, newWaterList]

def dfs():    
    queue = deque([[dataMap, startPoint, 0]])

    checkList = {}
    waterFind = {0: makeWater(waterMap, waterList)}
    
    while queue:
        left = queue.popleft()
        pr = left[0].split(',')
        
        # 이미 간 길 or 물 continue
        if left[2] not in waterFind:
            waterFind[left[2]] = makeWater(waterFind[left[2]-1][0], waterFind[left[2]-1][1])
        
        if left[0] in checkList:
            continue
        checkList[left[0]] = 0
        firstLoc = left[1][0]*C + left[1][1]
        for dir in direction:
            new_y = left[1][0] + dir[0]; new_x = left[1][1] + dir[1]
            
            if isOutOfRange(new_y, new_x):
                continue

            temp = left[0].split(',')
            secondLoc = new_y*C+new_x
        
            if waterFind[left[2]][0][new_y][new_x] == '*' \
                or temp[secondLoc] == 'X':
                continue
            
            if temp[secondLoc] == 'D':
                return left[2]+1
            
            
            temp[firstLoc], temp[secondLoc] = temp[secondLoc], temp[firstLoc]
            temp = ','.join(temp)
            queue.append([temp, [new_y, new_x], left[2]+1])
            
            
    return "KAKTUS"

print(dfs())