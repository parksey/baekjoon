from collections import deque

M, N = map(int,input().split())
tomato = []
dir = [[0,-1],[-1,0],[0,1],[1,0]]

old_q = deque([])
new_q = deque([])
minus=0
for i in range(N):
    tomato.append(list(map(int, input().split())))
    
    for j in range(M):
        if tomato[i][j]==1:
            old_q.append([i,j])
        elif tomato[i][j] == -1:
            minus += 1
         
def solve():   
    global old_q, new_q
    count = 0
    one_count = len(old_q)
    while old_q:
        old_left = old_q.popleft()
        
        for d in dir:
            y = old_left[0] + d[0]; x = old_left[1]+d[1]
            if y>=N or y<0 or x>=M or x<0:
                continue
            
            if tomato[y][x]:
                continue
            
            new_q.append([y,x])
            tomato[y][x] = 1
            one_count+=1
        if not old_q:
            if count == 0 and not new_q:
                return 0
            
            old_q = new_q
            new_q = deque([])

            count +=1
            
            if one_count + minus == M*N:
                return count
    
    return -1
    
print(solve())
