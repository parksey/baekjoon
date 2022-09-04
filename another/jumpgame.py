board = [
    [2,5,1,6,1,4,1],
    [6,1,1,2,2,9,3],
    [7,2,3,2,1,3,1],
    [1,1,3,1,7,1,2],
    [4,1,2,3,4,1,2],
    [3,3,1,2,3,4,1],
    [1,5,2,9,4,7,0]
]


def find(x,y):
    if x >= xLen or y >= yLen:
        return False
    
    if x == xLen-1 and y == yLen-1:
        return True
    
    if dp[y][x] != -1:
        return  dp[y][x]

    dp[y][x] = find(x+board[y][x],y) or find(x,y+board[y][x])
    return dp[y][x]

yLen = xLen = len(board)
dp = [[-1]*xLen for i in range(yLen)]
print(find(0,0))
