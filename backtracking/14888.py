N = int(input())
n_list = list(map(int, input().split()))
oper = list(map(int, input().split()))

operate = '+'*oper[0] + '-'*oper[1]+'*'*oper[2]+'/'*oper[3]
length = len(operate)
check = [0 for i in range(length)]

first = True
max = 0
min = 0

def made(index, data):
    global min, max, first
    if index == N:
        if first:
            max = data
            min = data
            first = False
        else:
            if max < data:
                max = data
            elif min > data:
                min = data
        return

    for i in range(length):
        if not check[i]:
            check[i]=1
            if operate[i] =='+':
                made(index+1,data+n_list[index])
            elif operate[i] == '-':
                made(index+1,data-n_list[index])
            elif operate[i] == '*':
                made(index+1,data*n_list[index])
            elif operate[i] == '/':
                if data < 0:
                    made(index+1,-(data*(-1) // n_list[index]))
                else:
                    made(index+1,data//n_list[index])
            check[i]=0


made(1, n_list[0])
print(max)
print(min)