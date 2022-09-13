from collections import deque
N,K = map(int, input().split())

queue = deque([N])

loc = [0]*100001

max = abs(N-K)

def add(q,left,d):
    if left+d < 0 or left+d>100000:
        return
    if loc[left+d] == 0 or loc[left+d] > loc[left]+1:
        loc[left+d] = loc[left]+1
        q.append(left+d)
        
while queue:
    left = queue.popleft()
    
    if left < 0 or left > 100000 or loc[left] >= max:
        continue    
    add(queue,left,-1)
    add(queue,left,1)
    add(queue,left,left)

print(loc[K])