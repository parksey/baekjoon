N = int(input())

heap = [0 for i in range(N+1)]
index = 0

def add(temp):
    global index
    index += 1
    
    heap[index] = temp
    i = index
    while i > 1:
        t = i//2
        m = abs(heap[i])
        comp = abs(heap[t])
        if m > comp:
            return
        
        if m == comp and heap[i] > heap[t]:
                return
            
        heap[i], heap[t] = heap[t], heap[i]
        i = t

def remove():
    global index
    
    
    temp = heap[1]
    heap[1] = heap[index]
    heap[index] = 0
    index -= 1
    
    if index <= 0:
        index = 0
        return temp
    
    i=1
    next =2 
    while next <= index:
        n = abs(heap[next])
        now = abs(heap[i])
        if next == index:
            if n > now:
                return temp
            elif n == now:
                if heap[next] > heap[i]:
                    return temp
            
        else:
            # 아래가 항상 크다
            if n > now and abs(heap[next+1]) > now:
                return temp
            # 절대값이 작거나 같다
            if heap[i] == heap[next] and heap[i] == heap[next+1]:
                return temp

            if n > abs(heap[next+1]):
                next += 1
            elif n == abs(heap[next+1]): 
                if heap[next] > heap[next+1]:
                   next+=1
            
        heap[next], heap[i] = heap[i], heap[next]
        
        i = next
        next = i * 2
    
    return temp

for i in range(N):
    temp = int(input())
    
    if temp == 0:
        print(remove())
    else:
        add(temp)