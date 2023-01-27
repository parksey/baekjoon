T = int(input())

def fill(snail, line, y,x):
    for i in range(line):
        snail[y][x]

def solve():
    N = int(input())
    
    snail = [[0]*N for i in range(N)]
    
    line = N
    y = 0
    x = -1
    go = 1
    index = 1
    rowTurn = True
    
    while line >= 1:
        if rowTurn:
            for i in range(line):
                x += go
                snail[y][x] += index
                index += 1
            line-=1
        else:
            for i in range(line):
                y += go
                snail[y][x] += index
                index += 1
            go *= -1
        rowTurn = not rowTurn

    for i in range(N):
        print(*snail[i])
        
for i in range(T):
    print("#{}".format(i+1))
    solve()