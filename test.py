N, M = map(int, input().split())

def nm(datalist, startX, length):
    if length == M:
        print(" ".join(list(map(str, datalist))))
        return True
    
    for i in range(1, N+1):
        if i in datalist:
            continue
        datalist.append(i)
        nm(datalist, i+1, length+1)
        datalist.pop()

    return False

nm([], 1 ,0)