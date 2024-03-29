N = int(input())

chess = [0 for i in range(N)]
cnt = 0

def isDig(index):
    for j in range(index):
        if chess[index] == chess[j] or (abs(j-index) == abs(chess[j]-chess[index])):
            return False
    return True
    

def check(index):
    global cnt
    if index == N:
        cnt+=1
        return
    
    for i in range(N):
        chess[index] = i
        if isDig(index):
            check(index+1)        

check(0)
print(cnt)