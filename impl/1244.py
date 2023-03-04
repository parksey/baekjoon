'''
1~연속적 번호 붙어있는 스위치
스위치 = 켜지거나 꺼져

학생들에게 1개이상 스위치 개수 이하인 자연수를 하나씩

남학생 = 스위치 번호가 자기가 받은 수의 배수 => 스위치 상태 변경
여학생 = 자기가 받은 숳와 같은 번호가 붙은 스위치를 중심으로 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간
'''

switchCnt = int(input())

swList = list(map(int, input().split()))

human = int(input())

hList = [list(map(int, input().split())) for i in range(human)]

def man(data):
    for index in range(len(swList)):
        if (index+1) % data == 0:
            swList[index] = 1-swList[index]

def wom(data):
    index = data -1 
    left = index - 1
    right = index + 1
    
    swList[index] = 1 -swList[index]
    while True:
        if left < 0 or right >= switchCnt:
            break
        
        if swList[left] != swList[right]:
            break
        
        swList[left] = 1 - swList[left]
        swList[right] = 1 - swList[right]
        left -= 1
        right += 1
    

funcMap = {
    1: man,
    2: wom
}

for hum in hList:
    funcMap[hum[0]](hum[1])

for i in range(0,len(swList), 20):
    print(*swList[i:i+20])