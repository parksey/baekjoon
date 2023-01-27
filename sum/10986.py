N, M = map(int, input().split())

numList = list(map(int, input().split()))

addList = [0]*M
addSum = 0
count = 0

for num in numList:
    addSum += num
    addList[addSum%M] += 1


def calc(cnt):
    return int(cnt * (cnt-1) / 2)

count = addList[0]

for cnt in addList:
    count += calc(cnt)
print(count)
