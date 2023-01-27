N, S = map(int, input().split())
numberList = list(map(int, input().split()))

start = end = 0
minSum = 0
minLength = len(numberList) + 1

def setPart():
    global minLength
    minLength = min(minLength, end - start)

while True:
    if minSum >= S:
        setPart()
        minSum -= numberList[start]
        start += 1
    else:
        if end == len(numberList):
            break
        minSum += numberList[end]        
        end+=1

print(0 if minLength > len(numberList) else minLength)
    