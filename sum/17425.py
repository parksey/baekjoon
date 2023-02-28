'''
A의 약수의 합은 A의 모든 약수를 더한 값, f(A)
x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값이 g(x)

x=1
1

x=2
1
1 2

x= 3
1
1 2
1 3

x=4
1
1 2
1 3
1 2 4

x = 5
1
1 2
1 3
1 2 4
1 5

x=6
1
1 2
1 2 4
1 5
1 2 3 6

x=7
1
1 2
1 2 4
1 5
1 2 3 6
1 7

x=10
1 2 5 10

5
1
2
10
70
10000
'''
N = int(input())

dataList = [int(input()) for i in range(N)]

maxData = max(dataList)
sumDp = [0] *(maxData+1)
dp = [1]*(maxData+1)

def elementSum(index):
    ret = 0
    i = 1
    while index * i <= maxData:   
        dp[index * i] += index
        i+=1

def solve():
    sumDp[1] = 1
    for i in range(2,maxData+1):
        elementSum(i)
        sumDp[i] = sumDp[i-1] + dp[i]

solve()

for data in dataList:
    print(sumDp[data])