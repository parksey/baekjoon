from collections import deque

N, M = map(int,input().split())

item = []
for i in range(N+M):
    item.append(list(map(int, input().split())))
    
game = [0]*100
game[0] = 0
def solve():
    queue = deque([1])

    while queue:
        top = queue.popleft()
        
        if top > 100:
            continue
        
        if top >= 94:
            if (game[99] > game[top-1]+1 or game[99] == 0):
                game[99] = game[top-1]+1
            continue
        
        if (game[top+5] > game[top-1]+1) or game[top+5]==0:
            game[top+5] = game[top-1]+1
            queue.append(top+6)
        
        for it in item:
            if top + 6 < it[0]:
                continue
            
            if game[it[1]-1] > game[it[0]-1] + 1 or game[it[1]-1] == 0:    
                queue.append(it[1])
                game[it[1]-1] = game[it[0]-1] + 1
    return game[99]
print(solve())
            