T = int(input())

def solve():
    nList = list(map(int, input().split()))
    
    ret = nList[0]
    min = max =nList[0]
    length = len(nList)
    for i in range(1, length):
        ret += nList[i]
        
        if min > nList[i]:
            min = nList[i]
        if max < nList[i]:
            max = nList[i]

    return round((ret - min - max) / (length-2))
    

for i in range(T):
    print("#{} {}".format(i+1, solve()))
