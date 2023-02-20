N = int(input())

dataList = [list(map(int, input().split())) for i in range(N)]

dp = [[0 for _ in range(3)] for i in range(N)]

def solve():

    dp[0][0] = dataList[0][0] 
    dp[0][1] = dp[0][2] = 1000 * 1000 + 1

    for i in range(1, N):
        dp[i][0] = dataList[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = dataList[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = dataList[i][2] + min(dp[i-1][0], dp[i-1][1])
    r = min(dp[N-1][1], dp[N-1][2])

    dp[0][1] = dataList[0][1] 
    dp[0][0] = dp[0][2] = 1000 * 1000 + 1

    for i in range(1, N):
        dp[i][0] = dataList[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = dataList[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = dataList[i][2] + min(dp[i-1][0], dp[i-1][1])
    g = min(dp[N-1][0], dp[N-1][2])
    
    dp[0][2] = dataList[0][2] 
    dp[0][1] = dp[0][0] = 1000 * 1000 + 1

    for i in range(1, N):
        dp[i][0] = dataList[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = dataList[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = dataList[i][2] + min(dp[i-1][0], dp[i-1][1])
    b = min(dp[N-1][0], dp[N-1][1])
    print(min(r,g,b))
solve()

