N = int(input())

dp = [1 for i in range(10)]

def solve():
    
    for i in range(1,N):
        for index in range(8, -1,-1):
            dp[index] = (dp[index] + dp[index+1]) % 10007
    
solve()
print(sum(dp)% 10007)