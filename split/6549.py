# 7 2 1 4 5 1 3 3 
# 시간 초과
def split( map_list):
    
    ret = 0
    length = len(map_list)
    for i in range(length):
        temp = map_list[i]

        left = i
        right = i
        l_done = False
        r_done = False

        while not l_done or not r_done:
            if left >= 0 and not l_done:
                if temp > map_list[left]:
                    left += 1
                    l_done = True
                elif left == 0: # temp <= map_list[left] 전제
                    l_done = True
                else:
                    left -= 1
            else:
                l_done = True
                
            if right < length and not r_done:
                if temp > map_list[right]:
                    right -= 1
                    r_done = True
                elif right == length - 1:
                    r_done = True
                else:
                    right += 1
            else:
                r_done = True
        
        width = right - left + 1
        sq = width * temp
        
        if ret < sq:
            ret = sq
    return ret


result = []

while True:
    N, *map_list = map(int, input().split())
    if N == 0:
        break

    result.append(split(map_list))
    
for i in result:
    print(i)
