from collections import deque


N = int(input())
h1, h2 = map(int, input().split())
m = int(input())
relation = [[] for _ in range(N+1)]

for i in range(m):
    s,e = map(int, input().split())
    relation[s].append(e)
    relation[e].append(s)
    
def solve():
    visit = [0 for i in range(N+1)]
    
    queue = deque([[h1,0]])
    cnt = 0
    while queue:
        left =queue.popleft()
        if visit[left[0]] == 1:
            continue 
        visit[left[0]] = 1
        if left[0] == h2:
            cnt = left[1]
            break
        for s in relation[left[0]]:
            queue.append([s,left[1]+1])
    
    if cnt == 0:
        return -1
    return cnt
print(solve())