N = int(input())

arr = [i for i in range(N,0,-1)]
stack = []
comp = []
for i in range(N):
    comp.append(int(input()))

index = 0
result = []
while arr:
    stack.append(arr.pop())
    result.append("+")
    
    while stack and stack[-1] == comp[index]:
        result.append("-")
        stack.pop()
        index+=1    
        
if arr or stack:
    print("NO")
else:
    print('\n'.join(result))