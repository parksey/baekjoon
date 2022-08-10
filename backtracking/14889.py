import sys
input = sys.stdin.readline
N= int(input())

player_map = []
for i in range(N):
    player_map.append(list(map(int, input().split())))
    

max_n = N//2
min = 0
isFirst = True

A_cnt = 0
A = [0 for i in range(N)]

def calc():
    global isFirst, min
    aCombo = 0
    bCombo = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i]==1 and A[j]==1:
                aCombo += player_map[i][j] + player_map[j][i]
            elif A[i]==0 and A[j]==0:
                bCombo += player_map[i][j] + player_map[j][i]
    
    if isFirst:
        min = abs(aCombo-bCombo)
        isFirst = False
    else:
        temp = abs(aCombo-bCombo)
        if min > temp:
            min = temp
    return


def match(num):
    if num == max_n:
        calc()
        return

    for i in range(N):
        if A[i] == 0:
            A[i]=1
            match(num+1, i+1)
            A[i]=0

match(0)
print(min)