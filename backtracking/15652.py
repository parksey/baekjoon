N, M = map(int, input().split())
stack = list()
def combin(index,count):
    global stack
    if count == M:
        print(' '.join(stack))
        return
        
    for i in range(index,N):
        stack.append(str(i+1))
        combin(i,count+1)
        stack.pop()

combin(0,0)
