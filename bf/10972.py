N = int(input())
'''
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2


'''
dataList = list(map(int, input().split()))

def swap(index):
    for i in range(len(dataList)-1, index, -1):
        if dataList[index] < dataList[i]:
            dataList[index], dataList[i] = dataList[i], dataList[index]
            return 


def find():
    global dataList
    for i in range(len(dataList)-2, -1, -1):
        if dataList[i] < dataList[i+1]:
            swap(i)
            
            dataList = dataList[:i+1] + sorted(dataList[i+1:])
            
            return True
    return False
    
if find():
    print(*dataList)
else:
    print(-1)