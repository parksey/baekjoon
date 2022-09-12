N, K = map(int ,input().split())

data = []
for i in range(N):
    data.append(list(map(int, input().split())))
    
dp = [[0]*(K+1) for i in range(N)]

def find():
    for i in range(1,K+1):
        dp[0][i] = data[0][1] if data[0][0] <= i else 0

    for i in range(1,N):
        for j in range(1,K+1):
            if data[i][0] <= j:
                dp[i][j] = max(data[i][1]+dp[i-1][j-data[i][0]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

find()
print(dp[-1][-1])