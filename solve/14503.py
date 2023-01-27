N, M = map(int, input().split())
# 0북, 1동, 2남, 3서

r,c, dir = map(int, input().split())

dataMap = []
for i in range(N):
    dataMap.append(list(map(int, input().split())))
    
direction = [[-1,0], [0,1], [1,0], [0,-1]]

def makeLeft(left):
    return (left+3)%4

def isOutOfRange(newY, newX):
    return newY >= N or newY < 0 or newX >= M or newX < 0

count = 1
dataMap[r][c] = 2
while True:
    startDir = dir
    left = startDir
    isMove = False
    for i in range(4):
        left = makeLeft(left)
        y, x = direction[left]
        newY = r+y
        newX = c+x
        
        if isOutOfRange(newY, newX):
            continue
        
        if dataMap[newY][newX] == 1 or dataMap[newY][newX] == 2:
            continue
            
        dir = left
        dataMap[newY][newX] = 2
        r = newY
        c = newX
        count+=1
        isMove = True
        break

    if (left == startDir) and not isMove:
        y, x = direction[startDir]
        r -= y
        c -= x
        
        if isOutOfRange(r,c) or dataMap[r][c] == 1:
            break

print(count)
        
        