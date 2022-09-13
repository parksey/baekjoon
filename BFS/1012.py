dir = [[-1,0],[1,0],[0,-1],[0,1]]

def check(ground, visit,i,j):
    stack = [[i,j]]
    
    
    while stack:
        top = stack.pop()
        
        if visit[top[0]][top[1]]:
            continue
        
        visit[top[0]][top[1]]=1
        
        for d in dir:
            y = top[0] + d[0]; x = top[1] + d[1]
            if y >= N or y < 0 or x>=M or x <0:
                continue
            if visit[y][x] or ground[y][x]==0:
                continue
            
            stack.append([y,x])
            

def find(ground, visit):
    count = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] or ground[i][j]==0:
                continue
            
            check(ground, visit,i,j)
            count+=1
    return count         

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())

    ground = [[0]*M for i in range(N)]
    visit = [[0]*M for i in range(N)]

    for j in range(K):
        x,y = map(int, input().split())
        ground[y][x] = 1
    
    print(find(ground, visit))
