from collections import deque


F,S,G,U,D = map(int ,input().split())

def solve():
    queue = deque([S])
    visit = [-1 for i in range(F+1)]
    visit[S]=0
    while queue:
        left = queue.popleft()
        
        if visit[G] != -1 and visit[G] < visit[left]:
            continue
        
        if left-D > 0:
            if visit[left-D] == -1 or visit[left-D] > visit[left]+1:
                queue.append(left-D)
                visit[left-D] = visit[left]+1
        if left+U <= F:
            if visit[left+U] == -1 or visit[left+U] > visit[left]+1:
                queue.append(left+U)
                visit[left+U] = visit[left]+1
    if visit[G] == -1:
        print("use the stairs")
    else:
        print(visit[G])
solve()