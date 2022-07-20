# 완전탐색 : 재귀, 경우의 수
N = int(input())

shape = [
    [[0,0],[0,1],[1,1]], # ㄱ
    [[0,0],[1,0],[0,1]],  # r
    [[0,0],[1,0],[1,1]], # ㄴ
    [[0,0],[1,0],[1,-1]], # _|
]

def boardcheck(board, H ,W):
    # 맵에서 다음 부분 재귀로 찾기 위해
    # 다음 변경
    x = -1
    y = -1
    for h in range(H):
        for w in range(W):
            if board[h][w] == '.':
                y = h
                x = w
                break
        if y != -1:
            break
    
    # 더 이상 변경 X
    if y == -1 or x == -1:
        return 1
    
    re = 0
    
    # ㄱ r ㄴ _| 의 모형 
    for s in shape:
        x_list = []
        y_list = []
        can = True
        for s_c in s:
            y_temp = y + s_c[0]
            x_temp = x + s_c[1]
            
            # 예외처리
            if y_temp >= H or y_temp < 0 or x_temp >= W or x_temp < 0:
                can = False
                break
            
            # 변경 불가
            if board[y_temp][x_temp] == '#':
                can = False
                break
            
            x_list.append(x_temp)
            y_list.append(y_temp)
        
        if can:
            # 변경할 수 있을 때 : 블럭이 들어갈 수 있을때
            for i in range(3):
                board[y_list[i]][x_list[i]] = '#'
            
            re += boardcheck(board, H ,W)
            
            for i in range(3):
                board[y_list[i]][x_list[i]] = '.'
    
    return re
    
result = []
for i in range(N):
    H, W = map(int, input().split())
    
    board = []
    for h in range(H):
        board.append([c for c in input()])
        
    result.append(boardcheck(board, H, W))
    
print(result)
    