# 8
# 1 8
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6

N = int(input())

li = []
for i in range(N):
    li.append(list(map(int, input().split())))
li.sort(key=lambda x: x[0])

dp = [1 for i in range(N)]

dp[0] = 1
for i in range(N):
    for j in range(i):
        if li[i][1] > li[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(N- max(dp))