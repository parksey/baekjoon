# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 1 2 4 3
# 1 2 3 4

# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1
# 3 1 2 5 4
# 3 1 4 2 5

from collections import deque

N, M, R = map(int, input().split())
node_map = {}
for i in range(M):
    u, v = map(int , input().split())
    
    if u not in node_map:
        node_map[u] = [v]
    else:
        node_map[u].append(v)
    
    if v not in node_map:
        node_map[v] = [u]
    else:
        node_map[v].append(u)
       
for k in node_map:
    node_map[k].sort()

def dfs(r):
    visit = [0] *N
    
    stack = [r]
    result = []
    while stack:
        top = stack.pop()
        
        if top not in node_map:
            break
        
        if visit[top-1]:
            continue
        
        visit[top-1] = 1
        result.append(top)
        
        for i in node_map[top][::-1]:
            if not visit[i-1]:
                stack.append(i)
    return result if result else [R]

def bfs(r):
    queue = deque([r])
    visit = [0] * N
    result= []
    while queue:
        first = queue.popleft()
        
        if first not in node_map:
            break
        
        if visit[first - 1]:
            continue
        
        visit[first - 1]= 1
        result.append(first)
        
        for i in node_map[first]:
            if not visit[i-1]:
                queue.append(i)
    return result if result else [R]
print(*dfs(R))
print(*bfs(R))
