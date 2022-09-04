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
