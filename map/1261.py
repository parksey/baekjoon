from collections import deque
M, N = map(int, input().split())

dataMap = []
for i in range(N):
    dataMap.append(list(input()))
    
direction = [[-1,0], [0,-1], [1,0], [0,1]]

def isOutOfRange(y,x):
    if y >= N or y < 0 or x >= M or x < 0:
        return True
    return False

def solve():
    checkList = [[-1 for i in range(M)] for j in range(N)]
    checkList[0][0]= 0
    
    queue = deque([[0,0]])

    while queue:
        y,x = queue.popleft()
        
        if y == N-1 and x == M-1:
            continue
        for dir in direction:
            new_y = y + dir[0]; new_x = x + dir[1]
            
            if isOutOfRange(new_y, new_x):
                continue
            
            nextStep = checkList[y][x] + (1 if dataMap[new_y][new_x] == '1' else 0)
            if checkList[new_y][new_x] == -1 or nextStep < checkList[new_y][new_x]:
                checkList[new_y][new_x] = nextStep
                queue.append([new_y, new_x])
    return checkList[-1][-1]
print(solve())
'''
01000
01010
00010

 0  1  1 -1 -1
 0  1  1 -1 -1
 0  0  0 -1 -1

'''
            