# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

from collections import deque


N = int(input())

branch = int(input())


node_map = {}
visit = [0] * N

for i in range(branch):
    n,v = map(int, input().split())
    
    if n in node_map:
        node_map[n].append(v)
    else:
        node_map[n] = [v]
        
    if v in node_map:
        node_map[v].append(n)
    else:
        node_map[v] = [n]


def find():
    global node_map
    
    queue = deque([1])
    visit[0] = 1
    count = 0
    
    while queue:
        first = queue.popleft()
        count+=1
        print(queue, visit)
        if first not in node_map:
            return count
        
        for i in node_map[first]:
            if not visit[i-1]:
                queue.append(i)
                visit[i-1] = 1
    return count
        
print(find()-1)