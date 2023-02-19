N = int(input())

dataList = list(map(int, input().split()))
dp = [0]*N

def solve():
    dp = dataList.copy()
    for i in range(1,N):
        for j in range(i):
            if dataList[i] <= dataList[j]:
                continue
            
            if dp[i] < dataList[i] + dp[j]:
                dp[i] = dataList[i] + dp[j]

    print(dp)
    print(max(dp))
    
solve()