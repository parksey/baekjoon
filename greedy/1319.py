# N = int(input())

# dataList = [] 
# alphabetSet= []
# for i in range(N):
#     dataList.append(input())
    
#     for char in dataList[-1]:
#         if char not in alphabetSet:
#             alphabetSet.append(char)

# alphaLength = len(alphabetSet)
# ret = 0  
# def make(numList):
#     result = {}
#     for i in range(len(alphabetSet)):
#         result[alphabetSet[i]] = numList[i]
#     return result
    
# def calc(numList):
#     global ret
#     result = 0
    
#     numberMap = make(numList)

#     for data in dataList:
#         numberString = ""
#         for d in data:
#             numberString += str(numberMap[d])

#         result += int(numberString)
    
#     ret = ret if ret > result else result
    
# def loop(numList):
#     if len(numList) == alphaLength:
#         calc(numList)
#         if numList[0] == 0:
#             print(numList)
#         return
#     for i in range(9,-1,-1):
#         if i not in numList:
#             numList.append(i)
#             loop(numList)
#             numList.pop()

# def solve():
#     loop([])
#     print(ret)
# solve()

N = int(input())

dataList = [] 
alphabetMap= {}
for i in range(N):
    dataList.append(input())
    
    for index, char in enumerate(dataList[-1][::-1]):
        if char not in alphabetMap:
            alphabetMap[char] = [0] * 8
        alphabetMap[char][index] +=1
        
scoreSort = []

def total(scoreList, num):
    ret = 0
    mul = 1
    for score in scoreList:
         ret += score * mul * num
         mul *= 10
    return ret

for alpha in alphabetMap:
    scoreSort.append([alpha, total(alphabetMap[alpha],1)])

scoreSort.sort(key = lambda x : -x[1])

ret = 0
for index, sc in enumerate(scoreSort):
    ret += total(alphabetMap[sc[0]], 9-index)
print(ret)
    