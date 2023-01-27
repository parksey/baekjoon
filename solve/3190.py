from collections import deque

# 동, 남, 서, 북
direction = [[0,1], [1,0], [0,-1], [-1,0]]


N = int(input())
mapList = [[0 for _ in range(N)] for __ in range(N)]

apple = int(input())
for _ in range(apple):
    y, x = map(int, input().split())
    mapList[y-1][x-1] = 1


def newDirection(rot):
    global curDir
    curDir = (curDir+rot+4) % 4

def outOfRange(y,x):
    return y >= N or y < 0 or x >= N or x <0

def move(afterSec, rot):
    global answer, snake
    
    for i in range(afterSec):
        answer += 1
        newY = snake[0][0] + direction[curDir][0]
        newX = snake[0][1] + direction[curDir][1]
       
        if outOfRange(newY, newX) or [newY, newX] in snake:
            return False
        
        snake.appendleft([newY,newX])
        
        if mapList[newY][newX] == 0:
            snake.pop()
        else:
            mapList[newY][newX] = 0
    
    if rot == 'D':
        newDirection(1)
    elif rot == 'L':
        newDirection(-1)
    return True

L = int(input())

answer = 0
curDir = 0
snake = deque([[0,0]])

def solve():
    for i in range(L):
        X, C = input().split()
        
        lastX = int(X) - answer
        if not move(lastX,C):
            return
    
    if not move(10001-answer, ""):
        return
solve()
print(answer)