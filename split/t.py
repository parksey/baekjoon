while True:
    N, *map_list = map(int, input().split())
    
    if N == 0:
        break
    
    temp = []
    ret = 0
    for i in range(N):
        while len(temp) != 0 and map_list[temp[-1]] > map_list[i]:
            t = temp.pop()
            print("temp : ",temp)
            if len(temp) == 0:
                width = i
            else:
                print("?")
                width = i - temp[-1] -1
                print(i, temp[-1])
            print("shape:",width,map_list[t])
            ret = max(ret, width*map_list[t])
        temp.append(i)

    print(ret)
    while len(temp) != 0:
        t = temp.pop()
        
        if len(temp) == 0:
            width = N
        else:
            width = N - temp[-1] -1
            
        ret = max(ret, width*map_list[t])
    print(ret)