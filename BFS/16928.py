from collections import deque

N, M = map(int,input().split())

item = {}
for i in range(N+M):
    s,e = map(int, input().split())
    item[s] = e
    
game = [0]*100
game[0] = 0
def solve():
    
    queue = deque([1])

    while queue:
        top = queue.popleft()
        take = False
        if top >= 100:
            continue
        
        if top >= 94:
            if (game[99] > game[top-1]+1 or game[99] == 0):
                game[99] = game[top-1]+1
            continue
        
        
        for it in item:
            if not (top + 1 <= it and top + 6 >= it): # top +1 보다 크고 top+6보다 작다
                continue
            step = it
            while step in item:
                step = item[step]
                
            if game[step-1] > game[top-1] + 1 or game[step-1] == 0:    
                queue.append(step)
                game[step-1] = game[top-1] + 1
                
                if top+6 == it:
                    take = True
        
        to = top
        if take:
            to-=1
            if (game[to+5] > game[top-1]+1) or game[to+5]==0:
                game[to+5] = game[top-1]+1
                queue.append(to+6)    
        if (game[top+5] > game[top-1]+1) or game[top+5]==0:
            game[top+5] = game[top-1]+1
            queue.append(top+6)
    
    return game[99]
print(solve())
            