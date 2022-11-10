N = int(input())

nList = [0]*(N+1)

NUMBER = ['3', '6', '9']

def solve():
    if N <= 3:
        nList[3] = 1
        return
    if N <= 6:
        nList[6] = 1
        return
    if N <= 9:
        nList[9] = 1
        return
    
    nList[3] = nList[6] = nList[9] = 1

    for i in range(10,N+1):
        strNum = str(i)
        nList[i] = nList[int(strNum[1:])]
        if strNum[0] in NUMBER:
            nList[i] +=1
    
    return

solve()
result = ""
for i in range(1,N+1):
    if nList[i] == 0:
        result += str(i)
    else:
        result += "-"*nList[i]
    result += " "

print(result[:-1])
