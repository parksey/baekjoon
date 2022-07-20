# 완전 탐색 : 재귀, 경우의 수
N = int(input())

# 재귀 count return하는 방법
# 재귀를 통해 받아온 값을 return
def pair(friends_map, n_list,n):
    finish = -1
    for i in range(n):
        if n_list[i] == 0:
            finish = i
            break
    
    if finish == -1:
        return 1
    re = 0
    
    for i in range(finish,n):
        if n_list[i] != 1 and friends_map[finish][i] == 1:
            n_list[finish] = n_list[i] = 1

            re += pair(friends_map, n_list,n)
            n_list[finish] = n_list[i] = 0
    return re
            
result = []
for i in range(N):
    n, m = map(int, input().split())
    
    # 맵 매핑
    friends_map = [[0 for j in range(n)]for i in range(n)]
    
    main = True
    main_data = 0
    for d in list(map(int, input().split())):
        if main:
            main_data = d
        else:
            friends_map[main_data][d] = 1
            friends_map[d][main_data] = 1
        main = not main
    
    n_list = [0 for j in range(n)]

    result.append(pair(friends_map, n_list,n))

print(result)