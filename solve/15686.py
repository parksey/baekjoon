from collections import deque
N, M = map(int, input().split())

localMap = []
houseMap = []
chickenMap = []
result = 0

for i in range(N):
    localMap.append(list(map(int, input().split())))
    
    for j in range(N):
        if localMap[i][j] == 1:
            houseMap.append([i,j])
        elif localMap[i][j] == 2:
            chickenMap.append([i,j])            


def calcLength(house, chicken):
    return abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])

def calc(chickenList):
    # 치킨집 M개
    city = 0
    for house in houseMap:
        minHouse = 0
        # 각 집의 치킨 거리
        for chicken in chickenList:
            length = calcLength(house, chicken)
            if minHouse == 0 or minHouse > length:
                minHouse = length
        # 모든 치킨 거리의 합
        city += minHouse
    return city
    

def solve(chickenList, start):
    global result
    if len(chickenList) == M:
        city =calc(chickenList)
        if result == 0 or result > city:
            result = city
        return
        
    for i in range(start,len(chickenMap)):
        chickenList.append(chickenMap[i])
        solve(chickenList, i+1)
        chickenList.pop()
    
solve([],0)
print(result)
