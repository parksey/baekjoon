from collections import deque

def bfs(r):
    global visit
    if r not in data_map:
        return
    
    queue = deque([r])
    seq = 1
    visit[r-1] = seq
    while queue:
        first = queue.popleft()
        
        for d in data_map[first]:
            if visit[d-1] ==0:
                visit[d-1] = seq
                seq+=1
                queue.append(d) 
    
N, M, R = map(int, input().split())

data_map = {}
for _ in range(M):
    u, v = map(int, input().split())
    
    if u not in data_map:
        data_map[u] = [v]
    else:
        data_map[u].append(v)
    if v not in data_map:
        data_map[v] = [u]
    else:
        data_map[v].append(u)
        
for k in data_map:
    data_map[k].sort(reverse=True)
    
visit = [0 for i in range(N)]

bfs(R)

for i in visit:
    print(i)


# from collections import deque
# import sys
# input = sys.stdin.readline

# n,m,r = map(int,input().split())
# link = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
# visited[r] = 1
# cnt = 1
# q = deque([r])

# # 양방향 간선 생성
# for _ in range(m):
#     a,b = map(int,input().split())
#     link[a].append(b)
#     link[b].append(a)

# # 내림차순으로 정렬
# for i in range(1,n+1):
#     link[i].sort(reverse = True)
# print(link)
# while q:
#     v = q.popleft()
#     for i in link[v]:
#         # 큐에 새로 넣어줄 때 방문 여부를 체크한다.
#         if visited[i]:
#             continue
#         cnt+=1
#         visited[i] = cnt
#         q.append(i)
# print(*visited[1:], sep="\n")