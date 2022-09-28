from heapq import heappop, heappush

N = int(input())
M = int(input())

n_list = [[] for i in range(N+1)]
INF = 999999999

for i in range(M):
    a,b,c = map(int, input().split())
    
    n_list[a].append([b,c])
    
def find(visit, node):
    min = INF
    index =0 
    for i in range(1,N+1):
        if visit[i]: continue
        
        if min > node[i]:
            min = node[i]
            index = i
    return index
        
    
def solve(s):
    visit = [0] * (N+1)
    node = [INF] * (N+1)
    node[s] = 0
    for i in range(N):
        index = find(visit, node)
        visit[index] = 1
        
        for j in n_list[index]:
            if node[j[0]] > node[index] + j[1]:
                node[j[0]] = node[index] + j[1]
    return node

def solve2(s):
    queue = [s]
    node = [INF] * (N+1)
    node[s] = 0
    while queue:
        left = heappop(queue)
        
        for i in n_list[left]:
            if node[i[0]] > node[left] + i[1]:
                node[i[0]] = node[left] + i[1]
                
                heappush(queue,i[0])
        
    for i in range(1,N+1):
        if node[i] == INF:
            node[i]='0'
        else:
            node[i]=str(node[i])
    return node
        

for i in range(1,N+1):
    print(' '.join(solve2(i)[1:]))