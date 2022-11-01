N = int(input())

nList = []
for i in range(N):
    nList.append(N)
    
nList.sort()


result = abs(nList[0]+nList[N-1])
first = nList[0]
second = nList[N-1]

for i in range(N):
    temp = abs(nList[i] + nList[N-1])
    for j in range(N-2,i,-1):
        if temp > abs(nList[i] + nList[j]):
            temp = nList[i] + nList[j]
            first = nList[i]
            second = nList[j]
        