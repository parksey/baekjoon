N, M = map(int, input().split())
stack = list()
isDone = [False for i in range(8)]
def combin(index,count):
    global stack
    if count == M:
        print(' '.join(stack))
        return
        
    for i in range(index,N):
        stack.append(str(i+1))
        if not isDone[i]:
            isDone[i] = True   
            combin(i, count+1)
            isDone[i] = False
        stack.pop()

combin(0,0)
