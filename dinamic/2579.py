N = int(input())
stair = [int(input()) for i in range(N)]
n = [0 for i in range(N)]

def find():
    if N == 1:
        return stair[0]
    n[0] = stair[0]
    n[1] = stair[1] + stair[0]
    if N == 2:
        return n[1]
    
    n[2] = stair[2]+(stair[0] if stair[0] > stair[1] else stair[1])
    if N==3:
        return n[2]
    
    for i in range(3,N):
        n[i] = stair[i] + (n[i-2] if n[i-2] > stair[i-1] + n[i-3] else stair[i-1] + n[i-3])
    return n[N-1]

print(find())