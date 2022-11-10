T = int(input())

def ro90(gMap, N, start):
    ret =""
    for i in range(N-1,-1,-1):
        ret += gMap[i][start]
    return ret

def ro270(gMap, N, start):
    ret =""
    for i in range(N):
        ret += gMap[i][N-1-start]
    return ret

def solve():
    N = int(input())
    
    gMap = []
    for i in range(N):
        gMap.append(input().split())
    
    rotate90 = []
    rotate180 = []
    rotate270 = []

    for i in range(N):
        rotate90.append(ro90(gMap, N, i))
        
        rotate180.append(''.join(gMap[N-1-i][::-1]))
        
        rotate270.append(ro270(gMap, N, i))
    
    for i in range(N):
        print("{} {} {}".format(rotate90[i], rotate180[i], rotate270[i]))

for i in range(T):
    print("#{}".format(i+1))
    solve()