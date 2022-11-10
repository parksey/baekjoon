T = int(input())

def row(gMap, loc, N, K):
    cnt = 0
    for i in range(loc[1],N):
        if gMap[loc[0]][i] == 0:
            break
        
        cnt+=1
        if cnt > K:
            return False
        
    return cnt == K
    
def col(gMap, loc, N, K): 
    cnt = 0
    for i in range(loc[0],N):
        if gMap[i][loc[1]] == 0:
            break
        
        cnt += 1
        if cnt > K:
            return False
        
    return cnt == K

def solve():
    N, K = map(int, input().split())
    
    gMap = []
    
    for i in range(N):
        gMap.append(list(map(int, input().split())))
        
    cnt = 0
    for i in range(N):
        for j in range(N):
            if gMap[i][j] == 0:
                continue
            
            if not (j != 0 and gMap[i][j-1] == 1):
                cnt += 1 if row(gMap, [i,j], N, K) else 0
            
            if not (i != 0 and gMap[i-1][j] == 1):
                cnt += 1 if col(gMap, [i,j], N, K) else 0
    return cnt            

for i in range(T):
    print("#{} {}".format(i+1, solve()))