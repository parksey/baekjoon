N, M = map(int, input().split())

branch = list(map(int, input().split()))

def cut(mid):
    ret = 0
    for i in branch:
        if i // mid != 0:
            ret += (i-mid)
    return ret

def find(start, end):
    if start > end:
        return end
    elif start == end:
        cutting = cut(end)
        if cutting < M:
            return -1
        return end 
    
    mid = (start+ end)//2
    cutting =  cut(mid)
    if cutting > M:
        ret = find(mid+1, end)
        if ret == -1:
            ret = mid
        return ret
    elif cutting < M:
        return find(start, mid - 1)
    else:
        return mid
    
max_data =max(branch)
result = find(1, max_data)
if max_data == result:
    print(result - 1)
else:
    print(result)
