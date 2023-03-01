'''
N x N
땅에는 나라가 하나씩

r행 c열 : A[r][c]명이 살고있다.
모든 국경선은 정사각형

1. 국경선 공유, L <= 차이 <= R 오늘 하루동안 연다.
2. 국경선이 모두 열리면 인구 이동
3. 인접한 칸만 이용해 이동할 수 있으면 그 나라를 오늘 하루 연합
4. 엽합을 이루고 있는 각 칸의 인구수 = (연합의 인구수) / 연합 칸의 개수
'''

N, L, R = map(int, input().split())

dataList = [list(map(int, input().split())) for i in range(N)]

def isOutOfRange(y,x):
    if y >= N or y < 0 or x >= N or x < 0:
        return True
    return False
   
def canMoveRange(origin, new_y, new_x):
    po = abs(dataList[origin[0]][origin[1]] - dataList[new_y][new_x])
    if po >= L and po <= R:
        return True
    return False
    
    
def dfs(i,j, checkList):
    stack = [[i,j]]
    direction  = [[-1,0], [0,-1], [1,0], [0,1]]
    unionStack = []
    total = 0
    while stack:
        top = stack.pop()
        
        if checkList[top[0]][top[1]] == 1:
            continue
        
        checkList[top[0]][top[1]] = 1
        total += dataList[top[0]][top[1]]
        unionStack.append(top)
        
        for dir in direction:
            new_y = top[0] + dir[0]; new_x = top[1] + dir[1]
            
            if isOutOfRange(new_y, new_x):
                continue
            
            if not canMoveRange(top, new_y, new_x):
                continue
            
            stack.append([new_y, new_x])

    div = int(total / len(unionStack))
    for i in range(len(unionStack)):
        dataList[unionStack[i][0]][unionStack[i][1]] = div
    
    if len(unionStack) == 1:
        return False
    
    return True
            
            

def check():
    ret = False
    checkList = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if checkList[i][j] == 1:
                continue
            if dfs(i,j, checkList):
                ret = True
    return ret

def solve():
    year = 0
    while True:
        if not check():
            break
        year += 1
    return year
print(solve())