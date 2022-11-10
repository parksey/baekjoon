T = int(input())

def fill(snail, line, y,x):
    for i in range(line):
        snail[y][x]

def solve():
    N = int(input())
    
    snail = [[0]*N for i in range(N)]
    
    line = N
    y = x = 0
    index = 1
    go = 1
    
    colTurn = False
    
    while line >= 1:
        fill(snail, line, y, x)
        

for i in range(T):
    print("#{}".format(i+1))
    solve()