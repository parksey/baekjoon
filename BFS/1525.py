from collections import deque
dataList = []
correctState = "1,2,3,4,5,6,7,8,0"

startLoc = []
for i in range(3):
    data = input().split()
    
    for j in range(3):
        if data[j] == '0':
            startLoc = [i,j]
    dataList.append(','.join(data))
            
initState = ','.join(dataList)

def isOutOfRange(y, x):
    if y >= 3 or y <0 or x>=3 or x < 0:
        return True
    return False

def solve():
    if initState == correctState:
        return 0
    
    direction = [[-1,0],[0,-1], [1,0],[0,1]]
    queue = deque([[initState, [startLoc[0], startLoc[1], 0]]])
    checkList = {initState:0}
    while queue:
        leftState, leftValues = queue.popleft()     
        
        if leftState == correctState:
            return leftValues[2]
            
        firstLoc = leftValues[0] * 3 + leftValues[1]
        
        
        for dir in direction:
            new_y = leftValues[0] + dir[0]; new_x = leftValues[1] + dir[1]
            if isOutOfRange(new_y, new_x):
                continue
            
            secondLoc = new_y*3 + new_x
            temp = leftState.split(",")
            temp[firstLoc], temp[secondLoc] = temp[secondLoc], temp[firstLoc]
            temp = ','.join(temp)
            if temp in checkList:
                continue
            
            checkList[temp] = 0
            queue.append([temp, [new_y,new_x, leftValues[2]+1]])
            
    return -1
            
print(solve())