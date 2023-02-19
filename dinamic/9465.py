'''
2

00
00

10
00

00
10

01
00

00
01

10
01

01
10

3

101
010

001
100

4
1010
0100\watch

'''

N = int(input())

def solve():
    k = int(input())
    
    dataList = [list(map(int, input().split())) for i in range(2)]
    
    dp = [[0 for i in range(k)] for _ in range(2)]

    dp[0][0] = dataList[0][0]
    dp[1][0] = dataList[1][0]
    
    if k == 1:
        return max(dp[0][0], dp[1][0])
    
    dp[0][1] = dataList[1][0] + dataList[0][1]
    dp[1][1] = dataList[0][0] + dataList[1][1]
    
    for i in range(2, k):
        dp[0][i] = dataList[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = dataList[1][i] + max(dp[0][i-1], dp[0][i-2])
    
    return (max(dp[0][-1], dp[1][-1]))

for i in range(N):
    print(solve())