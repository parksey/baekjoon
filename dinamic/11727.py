N = int(input())
dp = [0]*N
def solve():
    if N==1:
        return 1
    dp[0] = 1
    
    if N==2:
        return 3
    dp[1] = 3
    
    for i in range(2, N):
        dp[i] = dp[i-1] + dp[i-2]*2
    return dp[N-1]
    
print(solve()%10,007)