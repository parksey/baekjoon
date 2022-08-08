N = int(input())

chess = [0 for i in range(N)]

cnt = 0

def isDig(i,index):
    for j in range(index):
        if i == chess[j] or (abs(j-index) == abs(chess[j]-i)):
            return True
    return False
    

def check(index):
    global cnt
    if index == N:
        cnt+=1
        return
    
    for i in range(N):
        chess[index] = i
        if not isDig(i, index):
            check(index+1)        

check(0)
print(cnt)