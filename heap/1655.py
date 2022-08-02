N = int(input())

r_heap = [0 for i in range(N+1)]
l_heap = [0 for i in range(N+1)]
right = 0
left =0
mid = 0
iSRight = False

def max_heap(temp):
    global left
    left+=1
    
    i = left
    l_heap[i] = temp
    while i > 1:
        t = i // 2
        
        if l_heap[t] < l_heap[i]:
            l_heap[t], l_heap[i] = l_heap[i], l_heap[t]
        else:
            return
        i = t

def min_heap(temp):
    global right
    right += 1
    
    i = right
    r_heap[i] = temp
    while i > 1:
        t = i // 2
        
        if r_heap[t] > r_heap[i]:
            r_heap[t], r_heap[i] = r_heap[i], r_heap[t]
        else:
            return
        i = t
        

def find(temp):
    global left, right, mid
    
    if mid >= temp:
        #left
        if left == right:
            max_heap(temp)
        else:
            mid, temp = temp, mid
            min_heap(temp)
    else:
        #right
        if left == right:
            mid, temp = temp, mid
            max_heap(temp)
        else:
            min_heap(temp)
    
    return mid
    
    

for i in range(N):
    temp = int(input())
    if i == 0:
        max_heap(temp)
        print(l_heap[1])
    else:
        print(find(temp))
    print(l_heap)
    print(r_heap)
