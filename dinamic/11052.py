N  = int(input())

nList = list(map(int, input().split()))
 
dp = [0 for i in range(N+1)]

for totalCard in range(1,N+1):
    for card in range(1,N+1):
        if totalCard < card:
            continue
        
        dp[totalCard] = max(dp[totalCard], nList[card-1] + dp[totalCard - card])
        
print(dp)

'''
카드 N개
1번팩 1개, 2번팩 2개

돈을 최대한 많이 사용

'''