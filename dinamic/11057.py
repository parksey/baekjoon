N = int(input())

def solve():
    if N == 1:
        return 10
    
    dp = [[1 for _ in range(10)] for i in range(N)]
    for i in range(1,N):
        dp[i][0]=1
    
    for i in range(1,N):
        for j in range(1,10):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return sum(dp[N-1])
    
print(solve()%10007)