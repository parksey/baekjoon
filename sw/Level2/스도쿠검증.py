T = int(input())

MUL = 1
for i in range(1,10):
    MUL*=i

def row(gMap, start):
    sum=1
    for i in range(9):
        sum *= gMap[start][i]
    
    return sum != MUL

def col(gMap, start):
    sum=1
    for i in range(9):
        sum *= gMap[i][start]
    
    return sum != MUL

def round(gMap, y, x):
    sum = 1
    y *= 3
    x *= 3
    
    for i in range(3):
        for j in range(3):
           sum *= gMap[y+i][x+j]
    return sum != MUL

def solve():
    gMap = []
    for i in range(9):
        gMap.append(list(map(int, input().split())))
    
    
    for i in range(9):
        if row(gMap, i) or col(gMap, i) or round(gMap, i//3, i%3):
            return 0
    return 1
    
for i in range(T):
    print("#{} {}".format(i+1, solve()))