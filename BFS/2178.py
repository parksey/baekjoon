N, M = map(int, input().split())

miro = []
for i in range(N):
    miro.append(list(map(int,input())))
visit = [[0]*M for i in range(N)]
stack =[[0,0]]
dir = [[-1,0], [1,0], [0,-1], [0,1]]

visit[0][0] =1
while stack:
    top = stack.pop()
    
    for d in dir:
        y = top[0]+d[0]; x=top[1]+d[1]
        
        if y >=N or y <0 or x>=M or x<0:
            continue
        if miro[y][x]==0:
            continue
        
        if visit[y][x]==0 or visit[y][x] >visit[top[0]][top[1]]+1:
            visit[y][x] = visit[top[0]][top[1]]+1
            stack.append([y,x])

print(visit[-1][-1])