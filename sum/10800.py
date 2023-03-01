'''
[특정한 색]과 [크기]를 가진 자기 공 하나를 조종하여 게임 참여

목표 : 자기 공보다 크기가 작고 색이 다른 공을 사로잡아 공의 크기만큼 점수

1. 4
2. 3
3. 0
4. 1
'''

inputList = []
colorDict = {}
N = int(input())
answer = [0] * N

for i in range(N):
    color, size = map(int,input().split())
    inputList.append([color,size,i])
    
    if color not in colorDict:
        colorDict[color] = 0

inputList.sort(key = lambda x : x[1]) 

def solve():
    total = 0
    index = 0
    for i in range(N):
        while inputList[index][1] < inputList[i][1]:
             total += inputList[index][1]
             
             colorDict[inputList[index][0]] += inputList[index][1]
             index += 1
        answer[inputList[i][2]] = total - colorDict[inputList[i][0]]
solve()
print('\n'.join(map(str, answer)))