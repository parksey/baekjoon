from collections import deque

def bfs(r):
    global visit

    queue = deque([r])
    seq = 1
    while queue:
        first = queue.popleft()
        
        if first not in data_map or visit[first-1]:
            continue
        
        visit[first-1] = seq
        seq+=1
        
        for d in data_map[first]:
            if not visit[d-1]:
                queue.append(d)  
    if seq == 1:
        visit[r-1] = 1           
    
N, M, R = map(int, input().split())

data_map = {}
for _ in range(M):
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
    data_map[k] = sorted(data_map[k],reverse=True)
    
visit = [0 for i in range(N)]

bfs(R)

for i in visit:
    print(i)