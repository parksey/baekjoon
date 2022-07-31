N = int(input())

index = 0

heap = [0 for i in range(N+1)]

def remove():
    global index
    temp = heap[1]
    heap[1] = heap[index]
    heap[index] = 0
    if index <= 0:
        index =0
        return temp
    
    index -= 1
    
    i = 1
    next = 2
    isSame = False
    while next <= index:
        if next == index:
            if heap[next] > heap[i]:
                return temp
        else:
            if heap[next] > heap[i] and heap[next+1] > heap[i]:
                return temp
        
            if heap[next] > heap[next+1]:
                next += 1
        heap[next], heap[i] = heap[i], heap[next]
        
        i = next
        next *= 2
        
    return temp

def add(temp):
    global index
    index += 1
    heap[index] = temp
    
    i = index
    while i > 1:
        t = i //2
        if heap[i] > heap[t]:
            return
        
        heap[i], heap[t] = heap[t], heap[i]
        i = t

for i in range(N):
    temp = int(input())
    if temp == 0:
        print(remove())
    else:
        add(temp)