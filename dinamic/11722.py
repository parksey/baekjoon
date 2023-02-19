N = int(input())

dataList = list(map(int, input().split()))
dp = [1]*N

def solve():

    for i in range(1,N):
        for j in range(i):
            if dataList[i] >= dataList[j]:
                continue
            
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print(max(dp))
    
solve()