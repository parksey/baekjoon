'''
N x M 지도
r,c : r= 북쪽으로 부터, c = 서쪽으로부터 떨어진 칸의 개수

ㅜ : 1 5 6 2
ㅏ : 1 3 4
  2
4 1 3
  5
  6
  
->
  2
6 4 1
  5
  3
  
<-
  2
1 3 6
  5 
  4
  
ㅜ
  6
4 2 3
  1
  5
  
ㅗ
  1
4 5 3
  6
  2
'''
N, M, x, y, K = map(int, input().split())

dataMap = []
startLoc = [x,y]
for i in range(N):
    dataMap.append(list(map(int, input().split())))
    
commandList = list(map(int, input().split()))
dice = [[0 for i in range(3)] for j in range(4)]

def up():
    temp = dice[0][1]
    for i in range(1,4):
        dice[i-1][1] = dice[i][1]
    dice[-1][1] = temp

def down():
    temp = dice[3][1]
    for i in range(3,0,-1):
        dice[i][1] = dice[i-1][1]
    dice[0][1] = temp

def right():
    temp = dice[1][2]
    for i in range(2,0,-1):
        dice[1][i] = dice[1][i-1]
    dice[1][0] = dice[-1][1]
    dice[-1][1] = temp
    
def left():
    temp = dice[1][0]
    for i in range(2):
        dice[1][i] = dice[1][i+1]
    dice[1][-1] = dice[-1][1]
    dice[-1][1] = temp
    
direction = {
    1: [[0,1],right],
    2: [[0,-1],left],
    3: [[-1,0],up],
    4: [[1,0],down]
}

def outOfRange(x, y):
    if x >= N or x < 0 or y >= M or y < 0:
        return True
    return False

for command in commandList:
    dir, rollFunc = direction[command]
    next_x = startLoc[0] + dir[0]; next_y = startLoc[1] + dir[1]
    
    if outOfRange(next_x, next_y):
        continue
    
    rollFunc()
    
    if dataMap[next_x][next_y] == 0:
        dataMap[next_x][next_y] = dice[-1][1]
    else:
        dice[-1][1] = dataMap[next_x][next_y]
        dataMap[next_x][next_y] = 0
    startLoc = [next_x, next_y]
    print(dice[1][1])