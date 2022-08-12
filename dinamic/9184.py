reMap = [[[0 for _ in range(21)] for __ in range(21)] for ___ in range(21)]
def find(a,b,c):
    if a<= 0 or b<=0 or c<=0:
        reMap[0][0][0] = 1
        return 1
    
    if a>20 or b>20 or c>20:
        return find(20,20,20)
    
    if reMap[a][b][c] != 0:
        return reMap[a][b][c]
    
    if a<b and b<c:
        reMap[a][b][c] = find(a,b,c-1) + find(a,b-1,c-1) - find(a,b-1,c)
    else:
        reMap[a][b][c] =find(a-1,b,c) + find(a-1,b-1,c) +find(a-1,b,c-1) - find(a-1,b-1,c-1)
    return reMap[a][b][c]

while True:
    a,b,c = map(int, input().split())
    
    if a==-1 and b==-1 and c==-1:
        break
    
    print("w({}, {}, {}) = {}".format(a,b,c,find(a,b,c)))