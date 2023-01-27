T = int(input())

n = int(input())
aList = list(map(int,input().split()))

m = int(input())
bList = list(map(int,input().split()))

def addSum(partSum, returnList):
    if partSum not in returnList:
        returnList[partSum] = 1
    else:
        returnList[partSum] += 1

def getSumList(k, li):
    returnList = {}
    for i in range(k):
        partSum = li[i]
        addSum(partSum, returnList)
            
        for j in range(i+1,k):
            partSum += li[j]
            addSum(partSum, returnList)
            
    return returnList
aSum = getSumList(n, aList)
bSum = getSumList(m, bList)

count = 0
for a in aSum.keys():
    bT = T - a
    if bT in bSum:
        count += aSum[a] * bSum[bT]

print(count)