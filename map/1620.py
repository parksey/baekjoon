N, M = map(int, input().split())

encyclopedia = []
num = {}
for i in range(N):
    pokemon = input()
    encyclopedia.append(pokemon)
    num[pokemon] = i+1

def isNumber(inp):
    for i in inp:
        if not (i >= '0' and i<='9'):
            return False
    return True

for i in range(M):
    find = input()
    if isNumber(find):
        print(encyclopedia[int(find)-1])
    else:
        print(num[find])