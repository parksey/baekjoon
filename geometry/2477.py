# 7
# 4 50
# 2 160
# 3 30
# 1 60
# 3 20
# 1 100
# 동 1 서 2 남 3 북 4

N = int(input())

max_x = x =0
max_y = y =0

direction = ''

arr = [[] for i in range(4)]

for i in range(6):
    dir, cm = map(int, input().split())
    
    direction += str(dir)
    arr[dir-1].append(cm)

if len(arr[0]) == 2:
    max_x = arr[1][0]
    
    if len(arr[2]) == 2:
        max_y = arr[3][0]
        
        if "3131" in direction:
            x = arr[0][0]
            y = arr[2][1]
        elif '131' in direction:
            x = arr[0][0]
            y = arr[2][0]
        elif '313' in direction:
            x = arr[0][1]
            y = arr[2][1]
        else:
            x = arr[0][1]
            y = arr[2][0]
    else:
        max_y = arr[2][0]
        
        if "1414" in direction:
            x = arr[0][1]
            y = arr[3][0]
        elif '414' in direction:
            x = arr[0][0]
            y = arr[3][0]
        elif '141' in direction:
            x = arr[0][1]
            y = arr[3][1]
        else:
            x = arr[0][0]
            y = arr[3][1]
else:
    max_x = arr[0][0]
    
    if len(arr[2]) == 2:
        max_y = arr[3][0]
        
        if "2323" in direction:
            x = arr[1][1]
            y = arr[2][0]
        elif '323' in direction:
            x = arr[1][0]
            y = arr[2][0]
        elif '232' in direction:
            x = arr[1][1]
            y = arr[2][1]
        else:
            x = arr[1][0]
            y = arr[2][1]
    else:
        max_y = arr[2][0]
        
        if "4242" in direction:
            x = arr[1][0]
            y = arr[3][1]
        elif '242' in direction:
            x = arr[1][0]
            y = arr[3][0]
        elif '424' in direction:
            x = arr[1][1]
            y = arr[3][1]
        else:
            x = arr[1][1]
            y = arr[3][0]
        
print((max_x * max_y -x * y)*N)