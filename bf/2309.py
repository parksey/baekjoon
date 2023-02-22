dataList = [int(input()) for i in range(9)]

def find(result, start):
    if len(result) == 7 and sum(result) == 100:
        return True
    
    for i in range(start,len(dataList)):
        result.append(dataList[i])
        if find(result, i+1):
            return True
        result.pop()
        
    return False

def solve():
    result = []
    
    find(result, 0)
    result.sort()
    print('\n'.join(list(map(str,result))))
    
solve()