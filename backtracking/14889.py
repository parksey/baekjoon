N= int(input())

player_map = []
for i in range(N):
    player_map.append(list(map(int, input().split())))
    
max_n = N//2
min = 0
isFirst = True

A = []
check = [0 for i in range(N)]

def calc(B):
    global isFirst, min
    aCombo = 0
    bCombo = 0
    for i in range(max_n):
        for j in range(i+1,max_n):
            aCombo += player_map[A[i]][A[j]] + player_map[A[j]][A[i]]
            bCombo += player_map[B[i]][B[j]] + player_map[B[j]][B[i]]
    
    if isFirst:
        min = abs(aCombo-bCombo)
        isFirst = False
    else:
        temp = abs(aCombo-bCombo)
        if min > temp:
            min = temp
    return


def match(num,index):
    if num == max_n:
        B = []
        for i in range(N):
            if i not in A:
                B.append(i)
        calc(B)

        return

    for i in range(index,N):
        A.append(i)
        match(num+1,i+1)
        A.pop()

match(0,0)
print(min)