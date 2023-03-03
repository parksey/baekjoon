'''
트리

노드 부터 노드 까지으 ㅣ거리
'''
from collections import deque
T = int(input()) 

def setMap(K, graph, in_degree):
    for i in range(K):
        start, end = map(int, input().split())
        
        graph[start].append(end)
        in_degree[end] += 1
            
def solve():
    N, K = map(int ,input().split())
    dataList = list(map(int, input().split()))
    
    graph = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)
    dpMap= [0] * (N+1)
    
    setMap(K, graph,in_degree)

    endPoint = int(input())
    
    queue = deque([])
    
    for key in range(1,N+1):
        if in_degree[key] == 0:
            queue.append(key)
            dpMap[key] = dataList[key-1] 
    
    while queue:
        left = queue.popleft()
        
        if left == endPoint:
            break
        
        for key in graph[left]:
            in_degree[key] -= 1
            
            dpMap[key] = max(dpMap[key], dpMap[left] + dataList[key-1])
            if in_degree[key] == 0:
                queue.append(key)
    print(dpMap[endPoint])
                
for _ in range(T):
    solve()
    