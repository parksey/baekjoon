N, M = map(int, input().split())

gMap = [list(map(int, input().split())) for _ in range(N)]
dir = [[0,-1], [-1,0], [0,1], [1,0]]
checkMap = [[0 for _ in range(M)] for __ in range(N)]
checkMap[N-1][M-1] = 1

def dp(x, y):
    if checkMap[y][x] != 0:
        return checkMap[y][x]
    
    for d in dir:
            nextY = d[0]+y; nextX=d[1]+x
            
            if nextY >=N or nextY<0 or nextX>=M or nextX<0:
                continue
            
            if gMap[y][x] > gMap[nextY][nextX]:
                checkMap[y][x] += dp(nextX,nextY) 
    return checkMap[y][x]

# print(dp(M-1, N-1))
print(dp(0,0))