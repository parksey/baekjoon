V,E = map(int, input().split())

INF =999999999
v_list = [[] for i in range(V+1)] 

for i in range(E):
    a,b,c = map(int, input().split())
    v_list[a].append([b,c])
    
all_node = [[]]

def find(visit, node):
    min = INF
    index =0
    
    for i in range(1,V+1):
        if visit[i]: continue
        if min > node[i]:
            min = node[i]
            index = i
    return index

def solve(s):
    visit = [0] * (V+1)
    node = [INF] * (V+1)
    node[s] = 0
    for i in range(V):
        index = find(visit,node)
        visit[index] = 1
        
        for j in v_list[index]:
            if node[j[0]] > node[index] + j[1]:
                node[j[0]] = node[index] + j[1]
    return node
        
for i in range(1,V+1):
    all_node.append(solve(i))
    
min = INF
for i in range(1,V+1):
    for j in range(i+1,V+1):
        if min > all_node[i][j] + all_node[j][i]:
            min = all_node[i][j] + all_node[j][i]
if min == INF:
    print(-1)
else:
    print(min)
