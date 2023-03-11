R, C = map(int, input().split())
boardMap = [input().split() for i in range(R)]

direction = [[0,-1], [-1,0], [0,1], [1,0]]

def isOutOfRange(y,x):
    return y >= R or y < 0 or x >= C or x < 0

def visit(map, dy, dx):
    if map[dy][dx]:
        return True
    return False

def isExist(walkingList, data):
    if data in walkingList:
        return True
    return False
    

def solve(): 
    walkingList = []
    stack = [[0,0]]

    checkMap = [[0 for i in range(C)] for _ in range(R)]
    checkMap[0][0] = 1
    
    while stack:
        currLoc = stack.pop()
        
        if isExist(walkingList, boardMap[currLoc[0]][currLoc[1]]):
                continue
        walkingList.append(boardMap[currLoc[0]][currLoc[1]])
        
        for dir in direction:
            dy = currLoc[0] + dir[0]; dx = currLoc[1] + dir[1]
            
            if isOutOfRange(dy,dx) or visit(checkMap, dy, dx):
                continue
                            
            stack.append([dy, dx])
            checkMap[dy][dx] = 1
            
