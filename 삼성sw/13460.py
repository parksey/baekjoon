from collections import deque

N, M = map(int, input().split())

gMap = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
fRed= []
fBlue = []

for i in range(N):
    gMap.append(list(input()))
    for j in range(M):
        if gMap[i][j] == 'B':
            fBlue = [i,j]
        elif gMap[i][j] == 'R':
            fRed = [i,j]

loc = deque([[fRed, fBlue,0]])

def move(color, y,x):
    colorY = color[0]; colorX = color[1]
    while True:
        cy = colorY + y; cx = colorX + x

        if gMap[cy][cx] == '#':
            return [cy - y, cx - x, False]
        if gMap[cy][cx] == "O":
            return [cy,cx, True]

        colorY = cy; colorX = cx

def solve():
    mostMin = -1
    
    visit = [[fRed[0], fRed[1],fBlue[0], fBlue[1]]]
    while loc:
        red, blue, cnt = loc.popleft()
        
        if cnt > 10:
            return -1
        if mostMin != -1 and cnt >= mostMin:
            continue
        
        
        for i in range(4):
            redY = red[0]; redX = red[1]
            blueY = blue[0]; blueX = blue[1]

            newRy, newRx, redO = move([redY, redX], dy[i], dx[i])
            newBy, newBx, blueO = move([blueY, blueX], dy[i], dx[i])          
            # 원에 들어감
            if blueO:
                continue
                # blue O, red X
                # blue O, red O
            elif redO:
                # red만 들어감
                if mostMin == -1 or mostMin > cnt+1:
                    mostMin = cnt + 1
                continue
            
            # 안들어감8 8
            # 같은 위치에 있으면 한칸 뒤로
            if (newRx == newBx) and (newRy == newBy):
                if abs(newRy - redY) + abs(newRx - redX) > abs(newBy - blueY) + abs(newBx- blueX):
                    newRy -= dy[i]
                    newRx -= dx[i]
                else:
                    newBy -= dy[i]
                    newBx -= dx[i]
            
            if [newRy, newRx, newBy, newBx] not in visit:
                loc.append([[newRy, newRx], [newBy, newBx], cnt+1])
                visit.append([newRy, newRx, newBy, newBx])
    return mostMin
            

print(solve())
