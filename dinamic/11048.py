from collections import deque

N, M = map(int, input().split())

candyMap = [list(map(int, input().split())) for i in range(N)]

def solve():
    queue = deque([[0,0, candyMap[0][0]]])
    
    dir = [[0,1], [1,0], [1,1]]
    max = 0
    while queue:
        left = queue.popleft()
        
        if left[0] == N-1 and left[1] == M-1:
            max =  left[2] if max < left[2] else max
            continue
        
        for d in dir:
            y = d[0]+left[0]; x = d[1]+left[1]
            
            if y >= N or x>=M:
                continue
            
            queue.append([y,x, left[2]+candyMap[y][x]])
    print(max)
solve()