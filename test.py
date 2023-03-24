'''
기차 = 맨 앞에 있는 기관차 1대가 손님이 탄 객차 여러 칸을 끌고 간다.

소형 기관차 = 기관차가 고장나면 그것을 매꾸기 위한 기관차, 각 역 3대
1. 소형 기관차가 끌 수 있는 객차 수, 그 수보다 많으면 안된다.
2. 소형기관차 3대, 최대한 많은 손님 목적지 까지 운성
3. 각 소형차 번호가 연속적으로 이어진 객차를 끌게 한다.

Ex ) 객차 7칸
1대 최대 2칸
35 40 50 10 30 45 60
[35, 75, 90, 60, 40, 75, 105]

0   0   0   0   0   0   0
0   0   0   0   145 0   0
105 105 105 105 105 105 105  

1 : 1,2
2 : 3,4
3 : 6,7

객차 수 50,000이하
손님은 각차100명 이하 즉 최대 5,000,000

1 2 3 4 5  6  7  8  9  10 11
0 0 6 9 12 15 18 21 24 27 30

0 0 0 0 0  0  0  0  0  0  0 
0 0 0 0 0  0  0  0  0  0  0 
0 0 0 0 0  0  0  0  0  30  30 


'''

N = int(input())

humanList = list(map(int, input().split()))

maxSmall = int(input())

def calc(dp, sumList, index):
    
    for train in range(2, -1, -1):
 
        enp = maxSmall * (2 - train)
        stp = maxSmall * train
        if not (index >= stp and index < N - enp):
            dp[train][index] = dp[train][index+1]
            continue
        
        if train == 2:
            dp[train][index] = dp[train][index+1] if sumList[index] < dp[train][index+1] else sumList[index]
        else:
            temp = sumList[index] + dp[train+1][index+maxSmall]
            dp[train][index] = temp if dp[train][index+1] < temp else dp[train][index+1]
        
'''
0~2  0  2  4
2~4  1  1  2
4~6  2  0  0
'''
        

def solve():
    sumList = [0] * N
    
    sumList[0] = humanList[0]
    for i in range(1, maxSmall):
        sumList[i] = sumList[i-1] + humanList[i]

    for i in range(maxSmall, N):
        sumList[i] = sumList[i-1] + humanList[i] - humanList[i-maxSmall]
    
    dp =[[0 for i in range(N)] for j in range(3)]
    
    dp[-1][-1] = sumList[-1]
    for i in range(N-2, -1, -1):    
        calc(dp, sumList, i)
    
    for i in range(3):
        print(dp[i])
solve()

# N = int(input())
# humanList = list(map(int, input().split()))
# maxSmall = int(input())
# def calc(depth, index, sumList, ret):
#     if depth == 3:
#         return ret
#     result = 0
#     for i in range(index, N - maxSmall * (2 - depth)):
#         temp = calc(depth+1, i + maxSmall, sumList, ret + sumList[i])
#         result = result if result > temp else temp
#     return result
# def solve():
#     sumList = [0] * N
#     sumList[0] = humanList[0]
#     for i in range(1, maxSmall):
#         sumList[i] = sumList[i-1] + humanList[i]
#     for i in range(maxSmall, N):
#         sumList[i] = sumList[i-1] + humanList[i] - humanList[i-maxSmall]
#     print(calc(0, 0, sumList, 0))
# solve()