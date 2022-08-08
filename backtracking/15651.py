N, M = map(int, input().split())
stack = list()

def combin(count):
    global stack
    if count == M:
        print(' '.join(stack))
        return
        
    for i in range(N):
        stack.append(str(i+1))
        combin(count+1)
        stack.pop()

combin(0)
