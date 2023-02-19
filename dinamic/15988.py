'''
1 
1

2 
1 1
2

3 
1 1 1
1 2
2 1
3

4
3 + 1
2 + 2
1 + 3
'''
N = int(input())
inputList = [0]* N
for i in range(N):
    inputList[i] = int(input()) 

length = max(inputList)+1 
dp = [0] * (length)

def makeDp():
    dp[1] = 1
    if length == 2:
        return
    dp[2] = 2
    if length == 3:
        return
    dp[3] = 4
    if length == 4:
        return

    for i in range(4, length):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1_000_000_009

makeDp()
for k in inputList:
    print(dp[k])