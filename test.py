'''
[특정한 색]과 [크기]를 가진 자기 공 하나를 조종하여 게임 참여

목표 : 자기 공보다 크기가 작고 색이 다른 공을 사로잡아 공의 크기만큼 점수

1. 4
2. 3
3. 0
4. 1
'''


inputList = []
N = int(input())
for i in range(N):
    inputList.append(list(map(int,input().split())))

inputList.sort(key = lambda x: x[1])
print(inputList)