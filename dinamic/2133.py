'''
1 1

0
0

[1]
0

[2] + 2
0 0
0 0
1 1

1 1 + 2
0 0
0 0

1 1 + 1
1 1
1 1

(1,1,1)

[4]
0 0 1 1  0 0 0 0  0 0 1 1       0 1 1 0
0 0 1 1  0 0 0 0  0 0 0 0       0 1 1 0
1 1 1 1  1 1 1 1  1 1 0 0       1 1 1 1

1 1 1 1  1 1 1 1  1 1 0 0       1 1 1 1
0 0 1 1  0 0 0 0  0 0 0 0       0 1 1 0
0 0 1 1  0 0 0 0  0 0 1 1       0 1 1 0

1 1 1 1  1 1 0 0  1 1 1 1
1 1 1 1  1 1 0 0  1 1 0 0
1 1 1 1  1 1 1 1  1 1 0 0

(3,3,3, 2)

(9,9,9)
'''
N = int(input())

dp = [[0 for i in range(2)] for _ in range(N+1)] 

dp[2][0] = 3

for i in range(4,N+1,2):
    dp[i][0] = dp[i-2][0] * 3 + dp[i-2][1] +2
    dp[i][1] += dp[i-2][1] + (dp[i-2][0] *2)

print(dp[N][0]) 
