N = int(input())

n_list = sorted(list(map(int, input().split())))

X = int(input())

i = 0
j = N-1
cnt = 0
while i < j:
    comp = n_list[i] + n_list[j]
    if comp == X:
        cnt+=1
        j-=1
    elif comp < X: # 값을 더해줘야 한다.
        i+=1
    elif comp > X: # 값을 빼준다.
        j-=1
        
print(cnt)