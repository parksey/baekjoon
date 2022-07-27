# 7 2 1 4 5 1 3 3 
# 시간 초과
from inspect import stack

mapping = {
    "index": 0,
    "height": 1
}

def split( map_list):
    st = [[0,map_list[0]]]
    ret = st[0][mapping["height"]]
    length = len(map_list)
    
    for i in range(1, length):
        while st and st[-1][mapping["height"]] > map_list[i]:
            temp = st.pop()
            if not st:
                width = i
            else:    
                width = i - st[-1][mapping["index"]] - 1
            square = width * temp[mapping["height"]]
            
            if ret < square:
                ret = square
        
        st.append([i,map_list[i]])

    while st:
        temp = st.pop()
        
        if not st:
            width = length     
        else:    
            width = length - st[-1][mapping["index"]] - 1
        square = width * temp[mapping["height"]]
        
        ret = max(ret, square)

    return ret

result = []

while True:
    N, *map_list = map(int, input().split())
    if N == 0:
        break

    result.append(split(map_list))
    
for i in result:
    print(i)
