from collections import deque


N, K = map(int, input().split())

v = [-1] * (100001)

queue = deque([N])

v[N] = 0

while queue:
    left = queue.popleft()
    print(v[:5])
    if (left < 0) and left < 100001: continue
    
    if left *2 <= K*2 and  left*2 < 100001:
        if v[left*2] == -1 or v[left*2] > v[left]:
            queue.append(left*2); v[left*2] = v[left]
    if left +1 <= K:
        if v[left+1] == -1 or v[left+1] > v[left]+1:
            queue.append(left+1); v[left+1] = v[left]+1
    if left -1 >= 0:
        if v[left-1] == -1 or v[left-1] > v[left]+1:
            queue.append(left-1); v[left-1] = v[left]+1
print(v[K])