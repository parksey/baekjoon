def solution(wallpaper):
    y = len(wallpaper)
    x = len(wallpaper[0])
    answer = [y-1, x-1, 0, 0]
    

    
    for i in range(y):
        for j in range(x):
            if wallpaper[i][j] != '#':
                continue
            if answer[2] < i:
                answer[2] = i
            if answer[3] < j:
                answer[3] = j
            if answer[0] > i:
                answer[0] = i
            if answer[1] > j:
                answer[1] = j
    answer[2] +=1
    answer[3] +=1
    return answer