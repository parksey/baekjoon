import heapq

N = int(input())

dataList = [int(input()) for _ in range(N)]

heapq.heapify(dataList)

def solve():
    if N == 1:
        return heapq.heappop(dataList)
    result = 0
    for i in range(N-1):
        f = heapq.heappop(dataList)
        s = heapq.heappop(dataList)
        result += f+s
        heapq.heappush(dataList, f+s)
    return result
print(solve())
'''
10 40 100 200

(10+40) + (50+100) + (150 + 200) = 550

(10+40) + (100+200) + (50+300) = 
 
1 2 3 4 5 6 7 8 9

1+2 3+4 

1 1 1 1 1
1 1 1

'''