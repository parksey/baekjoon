N,M,R = map(int,input().split())

node = {}
for i in range(M):
    u, v = map(int, input().split())
    
    if u not in node:
        node[u] = [v]
    else:
        node[u].append(v)
    if v not in node:
        node[v] = [u]
    else:
        node[v].append(u)
    
     
for k in node:
    node[k] = sorted(node[k], reverse=True)

count = 0
visit=[0 for i in range(N)]

stack = [R]
while stack:
    top = stack.pop()
    if visit[top-1] == 0:
        count +=1
        visit[top-1] = count

    if top not in node:
        continue

    for n in node[top]:
        if visit[n-1] == 0:
            stack.append(n)

for i in visit:
    print(i)














from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
link = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[r] = 1
cnt = 1
q = deque([r])

# 양방향 간선 생성
for _ in range(m):
    a,b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)

# 내림차순으로 정렬
for i in range(1,n+1):
    link[i].sort(reverse = True)

while q:
    v = q.popleft()
    for i in link[v]:
        # 큐에 새로 넣어줄 때 방문 여부를 체크한다.
        if visited[i]:
            continue
        cnt+=1
        visited[i] = cnt
        q.append(i)
print(*visited[1:], sep="\n")