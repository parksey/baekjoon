from collections import deque

T = int(input())

dir = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]

def find(N, s, e):
    chess_map = [[0]*N for i in range(N)]

    queue = deque([s])
    
    while queue:
        left = queue.popleft()

        for d in dir:
            y = left[0] + d[0]; x = left[1] + d[1];
            if y >= N or y <0 or x>=N or x<0 or (y == s[0] and x ==s[1]):
                continue
            
            if chess_map[y][x]==0 or chess_map[left[0]][left[1]] +1 < chess_map[y][x]:
                chess_map[y][x] = chess_map[left[0]][left[1]] +1
                queue.append([y,x])
    
    return chess_map[e[0]][e[1]]
    
for i in range(T):
    N = int(input())
    
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    
    print(find(N, start, end))
    