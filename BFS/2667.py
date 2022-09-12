N = int(input())

in_map = []
for i in range(N):
    in_map.append(list(map(int, list(input()))))

visit = [[0]*N for i in range(N)]

dir = [[-1,0], [1,0], [0,-1], [0,1]] # 상하좌우 
re_cnt = []

def counting(i,j):
    stack = [[i,j]]
    result = 0
    
    while stack:
        top = stack.pop()
        
        if visit[top[0]][top[1]]:
            continue
        
        visit[top[0]][top[1]] = 1
        result+=1
        
        for d in dir:
            y=top[0]+d[0]; x=top[1]+d[1]
            
            if y<0 or y>=N or x<0 or x>=N:
                continue 
            if visit[y][x] or in_map[y][x]==0:
                continue

            stack.append([y,x])
    return result

def find():
    for i in range(N):
        for j in range(N):
            if visit[i][j] or in_map[i][j]==0:
                continue

            re_cnt.append(counting(i,j))
                  
find()
print(len(re_cnt))
for i in sorted(re_cnt):
    print(i)