'''
1
 1

2
 2

3
1 2
2 1
3

4
3+1
 1 2 1
 3 1
 
2+2
 
1+3
 1 3
 
5
4+1
 1 3 1
 
3+2
 2 1 2
 3 2
 
2+3
 2 3
 
6
5+1
 2 1 2 1
 3 2 1
 2 3 1
 
4+2
 1 2 1 2
 3 1 2
 1 3 2
 
3+3
 1 2 3
 2 1 3
 
7
6+1
 1 2 1 2 1
 3 1 2 1
 1 3 2 1
 1 2 3 1
 2 1 3 1

5+2
 1 3 1 2
 2 3 2
 
4+3
 1 2 1 3
 3 1 3
 

'''
import sys
input = sys.stdin.readline
N = int(input())

dp = [[0 for i in range(3)] for _ in range(100001)]

def dpInit():
    global dp
    dp[1][0], dp[1][1], dp[1][2] = 1,0,0
    dp[2][0], dp[2][1], dp[2][2] = 0,1,0
    dp[3][0], dp[3][1], dp[3][2] = 1,1,1
    
    for index in range(4, 100001):
        dp[index][0] = dp[index-1][1] % 1000000009 + dp[index-1][2] % 1000000009 
        dp[index][1] = dp[index-2][0] % 1000000009 + dp[index-2][2] % 1000000009 
        dp[index][2] = dp[index-3][0] % 1000000009 + dp[index-3][1] % 1000000009 
    

def solve(K):
    return sum(dp[K])% 1000000009


dpInit()

for i in range(N):
    print(solve(int(input())))