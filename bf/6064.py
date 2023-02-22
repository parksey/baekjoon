T = int(input())

def solve(M, N, x, y):
    if M == 1:
        if x != 1:
            return -1
        return y 
        
    if N == 1:
        if y != 1:
            return -1
        return x
    
    startX = x
    startY = y
    main = M
    sub = N
    
    if M > N:
        main = N
        sub = M
        startX = y
        startY = x
    print("main: sub", main,sub)
    cha = startY - 1
    step = -1
    div = sub % main # 23
    stepX = cha + 1 - div
    year = cha + 1 - sub
    
    while year <= M*N:
        step += 1
        year = step * sub + cha + 1
        stepX += div
        if stepX > main:
            stepX -= main
        '''
        1 1
        2 2
        3 3
        4 4
        5 1
        1 2
        2 3
        3 4
        4 1
        
        1 2 3 4 1 2 3 4
        '''
        print(year, step, sub, cha, stepX)
        
        if stepX == startX:
            return year
        
    return -1
    
    
for i in range(T):
    M, N, x, y = map(int, input().split())
    
    print(solve(M, N, x, y))