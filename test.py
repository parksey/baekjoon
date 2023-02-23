N = int(input())
'''
1 4 3 2


'''
dataList = list(map(int, input().split()))

def remove():
    data = dataList.pop()
    while data <= N:
        data += 1
        if data <= N and data not in dataList:
            dataList.append(data)
            return False
    return True

def add():
    length = len(dataList)
    if length == 0 or length > N:
        return False
    
    for i in range(1,N+1):
        if i not in dataList:
            dataList.append(i)
            return

def find():
    while dataList:
        if remove():
            continue
        
        if not add():
            break
        
    if not dataList:
        print(-1)
    else:
        print(*dataList)
    
find()