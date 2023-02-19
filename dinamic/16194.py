N  = int(input())

nList = list(map(int, input().split()))

dp = [0] *(N+1)

for totalCard in range(1,N+1):
    for card in range(1,N+1):
        if totalCard < card:
            continue
        
        if dp[totalCard] == 0 or dp[totalCard] > nList[card-1] + dp[totalCard-card]:
            dp[totalCard] = nList[card-1] + dp[totalCard-card]

print(dp)