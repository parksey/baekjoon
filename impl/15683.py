'''
N x M 크기의 직사각형으로

사무실에는 총 K개의 CCTV
CCTV는 5가지
'''
from collections import deque
N, M = map(int, input().split())

dataMap = []
cctvMap = []
notCount = 0
for i in range(N):
    data = input().split()
    
    for j in range(M):
        if data[j] >= '1' and data[j] <= '5':
            cctvMap.append([[i,j], data[j]])
            notCount += 1
        elif data[j] == '6':
            notCount += 1
    
    dataMap.append(','.join(data))
    
    
dataMap = ','.join(dataMap)


direction = [[-1,0], [0, -1], [1,0], [0, 1]]

def outOfRange(y, x):
    if y >= N or y < 0 or x >= M or x < 0:
        return True
    return False

def cctv1(queue, location):
    newQueue = deque([])
    
    while queue:
        left = queue.popleft()
        
        for i in range(4):
            dataList = left[0].split(',')
            
            cnt = do(location, dataList, direction[i])
            newQueue.append([','.join(dataList), left[1]+cnt])
    return newQueue
            

def cctv2(queue, location):
    newQueue = deque([])
    
    while queue:
        left = queue.popleft()
        
        for i in range(2):
            dataList = left[0].split(',')
            
            cnt = do(location, dataList, direction[i]) \
                + do(location, dataList, direction[i+2])
            newQueue.append([','.join(dataList), left[1]+cnt])
    return newQueue

def cctv3(queue, location):
    newQueue = deque([])
    
    while queue:
        left = queue.popleft()
        
        for i in range(4):
            dataList = left[0].split(',')
            
            cnt = do(location, dataList, direction[i]) \
                + do(location, dataList, direction[(i+1)%4])
            newQueue.append([','.join(dataList), left[1]+cnt])
    return newQueue


def cctv4(queue, location):
    newQueue = deque([])
    
    while queue:
        left = queue.popleft()
        
        for i in range(4):
            dataList = left[0].split(',')
            
            cnt = do(location, dataList, direction[i]) \
                + do(location, dataList, direction[(i+1)%4]) \
                + do(location, dataList, direction[(i+2)%4])    
            newQueue.append([','.join(dataList), left[1]+cnt])
    return newQueue


def cctv5(queue, location):
    newQueue = deque([])

    while queue:
        left = queue.popleft()
        
        dataList = left[0].split(',')

        cnt = do(location, dataList, direction[0]) \
            + do(location, dataList, direction[1]) \
            + do(location, dataList, direction[2]) \
            + do(location, dataList, direction[3])     
        newQueue.append([','.join(dataList), left[1]+cnt])
    return newQueue
        
def do(location, dataList, dir):
    cnt = 0
    curY = location[0]; curX = location[1]
    while True:
        curY+=dir[0]; curX+=dir[1]
        
        if outOfRange(curY, curX):
            break
        
        loc = curY*M+curX
        
        if dataList[loc] == '#':
            continue
        
        if dataList[loc] == '6':
            break
        
        if dataList[loc] == '0': 
            dataList[loc] = '#'
            cnt+=1
    return cnt
        
cctvFunc = {
    '1': cctv1,
    '2': cctv2,
    '3': cctv3,
    '4': cctv4,
    '5': cctv5
}


def solve():
    queue = deque([[dataMap,0]])

    for cctv in cctvMap:
        queue = cctvFunc[cctv[1]](queue, cctv[0])

    maxCount = max(queue, key=lambda x: x[1])[1]
    print(N*M - maxCount - notCount)
        
solve()