N = int(input())
n_list = list(map(int, input().split()))


for i in range(N):
    stack = [n_list[i]]
    
    for j in range(i+1,N):
        if stack[-1] < n_list[j]:
            stack.append(n_list[i])