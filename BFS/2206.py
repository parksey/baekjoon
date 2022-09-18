from collections import deque

N, M = map(int, input().split())

wall_map = []
for i in range(N):
    wall_map.append(list(input()))
    
dir = [[-1,0], [0,1],[1,0], [0,-1]]
def solve():
    queue = deque([[0,0,0]])
    visit = [[[0]*2 for j in range(M)] for i in range(N)]
    visit[0][0][0] = 1
    while queue:
        left = queue.popleft()
        for d in dir:
            brk = left[2]
            y = left[0]+d[0]; x = left[1]+d[1]
            
            if y >= N or y<0 or x>=M or x<0:
                continue
            
            if wall_map[y][x] == '1':
                if brk==1:
                    continue
                else:
                    brk = 1
            
            if visit[y][x][brk] == 0 or visit[y][x][brk]> visit[left[0]][left[1]][left[2]] + 1:
                queue.append([y,x,brk])
                visit[y][x][brk] = visit[left[0]][left[1]][left[2]] + 1
    if visit[N-1][M-1][0] == 0 and visit[N-1][M-1][1] == 0:
        return -1
    if visit[N-1][M-1][0] == 0:
        return visit[N-1][M-1][1]
    elif visit[N-1][M-1][1] == 0:
        return visit[N-1][M-1][0]
    return visit[N-1][M-1][0] if visit[N-1][M-1][0] < visit[N-1][M-1][1] else visit[N-1][M-1][1]

print(solve())