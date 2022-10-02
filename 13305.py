N = int(input())

road = list(map(int, input().split()))
prce = list(map(int, input().split()))

min = prce[0]
result = min*road[0]
cnt = 0
for i in range(1,len(road)):
    if prce[i] < min:
        result += cnt * min
        cnt = road[i]
        min = prce[i]
    else:
        cnt += road[i]
        
result += cnt * min
print(result)