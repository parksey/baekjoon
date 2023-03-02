'''
아기 상어
N x N
처음 아기 상어 크기 2
1초에 상하좌우

1. 자신보다 크기가 큰 물고기가 있는 칸은 지날 수 없다.
2. 나머지 칸은 모두 지날 수 있다.
3. 자신의 크기보다 작은 물고기만 먹을 수 있다. (크기가 같으면 지나갈 수는 있음)
4. 먹을 수 있는 물고기가 공간에 없다면 엄마 상어에게 도움을 요청
5. 먹을 수 있는 물고기가 1마리라면, 그 물고기
6. 1마리 보다 많으면 가장 가까운 물고기
7. 거리가 가까운 물고기 많으면 가장 위 물고기
8. 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기


'''
from collections import deque
N = int(input())

dataList = []
startLoc = []

for i in range(N):
    dataList.append(list(map(int, input().split())))
    
    for j in range(N):
        if dataList[-1][j] == 9:
            startLoc = [i,j, 0, 0]
            dataList[i][j] = 0



def isOutOfRange(y,x):
    if y >= N or y < 0 or x >= N or x < 0:
        return True
    return False    

def bfs(location, size):    
    queue = deque([location]) # y, x, timer, eat
    direction = [[-1,0], [0, -1], [0,1], [1,0]]
    checkList = [[0 for i in range(N)] for j in range(N)]
    temp = deque([])
    limitTime = -1
    while queue:
        left = queue.popleft()
        
        if limitTime != -1 and left[2] == limitTime:
            return deque(sorted(temp, key=lambda x: (x[2], x[0], x[1]))).popleft()
        
        if checkList[left[0]][left[1]] == 1:
            continue
        
        checkList[left[0]][left[1]] = 1
        
        for dir in direction:
            new_y = left[0] + dir[0]; new_x = left[1]+dir[1]
            
            if isOutOfRange(new_y, new_x):
                continue
            
            if dataList[new_y][new_x] > size:
                continue

            if dataList[new_y][new_x] < size and dataList[new_y][new_x] != 0:
                if limitTime == -1 or left[2] == limitTime:
                        limitTime = left[2] + 1
                temp.append([new_y, new_x, left[2]+1, left[3]+1])
            queue.append([new_y, new_x, left[2]+1, left[3]])
            
            
    return [-1,-1,0,0]
def solve():
    time = 0
    location = startLoc
    size = 2
    while True:
        location = bfs(location, size)
        dataList[location[0]][location[1]] = 0
        if location[0] == -1 and location[1] == -1:
            break

        time += location[2]
        location[2] = 0
        if location[3] == size:
            size += 1
            location[3] = 0
    return time
    
print(solve())