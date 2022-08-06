N, M = map(int, input().split())

n_list = set()
for i in range(N):
    n_list.add(input())
    
result = []
cnt = 0

for i in range(M): 
    temp = input()
    if temp in n_list:
        cnt+=1
        result.append(temp)
result.sort()
        
print(cnt)
for i in result:
    print(i)