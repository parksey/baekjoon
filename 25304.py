money = int(input())

N = int(input())
total = 0
for i in range(N):
    m, n = map(int, input().split())
    total += m*n
    
if total==money:
    print("Yes")
else:
    print("No")