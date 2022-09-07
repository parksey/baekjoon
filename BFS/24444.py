from collections import deque


def bfs(r):
    global visit
    queue = deque([r])
    seq = 1
    while queue:
        first = queue.popleft()
        print(visit)
        if visit[first-1] != 0:
            continue
        visit[first-1] = seq
        seq+=1
        for d in data_map[first]:
            queue.append(d)
            
        
    
    
N, M, R = map(int, input().split())

data_map = {}
for i in range(M):
    u, v = map(int, input().split())
    
    if u in data_map:
        data_map[u].append(v)
    else:
        data_map[u] = [v]
        
    if v in data_map:
        data_map[v].append(u)
    else:
        data_map[v] = [u]
        
for k in data_map:
    data_map[k].sort()
    
visit = [0] * N
bfs(R)

print(visit)



    