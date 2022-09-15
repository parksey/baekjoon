from collections import deque


M, N, H = map(int, input().split())


dir = [[-1,0,0], [0,1,0], [1,0,0],[0,-1,0],[0,0,1],[0,0,-1]]

def solve():
    tomato = []
    #[
    #     [[0]*M for i in range(N)] for j in range(H)
    # ]
    old_q = deque([])
    minus = 0
    for h in range(H): # 1
        tomato.append([])
        for n in range(N): # 3
            tomato[h].append(list(map(int,input().split())))
            for m in range(M): # 5
                if tomato[h][n][m] == 1:
                    old_q.append([m,n,h])
                elif tomato[h][n][m] == -1:
                    minus+=1
    
    count = 0
    new_q = deque([])
    comp = len(old_q)
    
    total = M*N*H
    
    while old_q:
        left = old_q.popleft()
        
        for d in dir:
            x = d[0]+left[0]; y = d[1]+left[1]; z=d[2]+left[2]
            
            if x>=M or x<0 or y>=N or y<0 or z>=H or z<0:
                continue
            
            if tomato[z][y][x]:
                continue
            
            tomato[z][y][x]=1
            new_q.append([x,y,z])
            comp+=1
            
        if not old_q: # 한번씩 다 본 후
            if count == 0 and not new_q:
                return count
            count += 1
            if comp+minus == total:
                return count
            
            
            old_q = new_q
            new_q = deque([])
        
    if comp+minus != total:
        return -1
    return count
      
print(solve())