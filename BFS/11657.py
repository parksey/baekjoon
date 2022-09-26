N,M = map(int,input().split())
INF = 9999999999

v = [INF] * (N+1)
v[1] = 0

node_map = [[] for i in range(N+1)]

for i in range(M):
    s,e,a = map(int,input().split())
    node_map[s].append([e,a])

def find(visit):
    min = INF
    index = 0
    for i in range(1, N+1):
        if min > v[i] and not visit[i]:
            index = i
            min = v[i]
    return index

def solve():
    visit = [0] * (N+1) 
    stack = []
    for i in range(N):
        index = find(visit)
        visit[index] = 1
        stack.append(index)
        for d in node_map[index]:
            if v[d[0]] > v[index]+d[1]:
                v[d[0]] = v[index] + d[1]

                    
    for s in stack:
        for d in node_map[s]:
            if v[s] == INF: continue
            if v[d[0]] > v[s]+d[1]:
                return -1
    
    return 0 
    

if solve() == -1:
    print(-1)
else:
    for i in v[2:]:
        if i == INF:
            print(-1)
        else:
            print(i)