N = int(input())

n_list = sorted(list(map(int, input().split())))

X = int(input())

print(n_list)
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
        
        
#         9
# 5 12 7 10 9 1 2 3 11
# 13

# 1 2 3 5 7 9 10 11 12