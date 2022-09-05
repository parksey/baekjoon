N, K = map(int ,input().split())

result = [[0 for __ in range(N)] for _ in range(N)]

data = []
for i in range(N):
    data.append(list(map(int, input().split())))
    
dp = [[0]*(K+1) for i in range(N+1)]

def find():
    for i in range(1,N+1):
        for j in range(1,K+1):
            if data[i-1][0] <= j:
                dp[i][j] = max(data[i-1][1]+dp[i-1][j-data[i-1][0]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
find()
print(dp[-1][-1])