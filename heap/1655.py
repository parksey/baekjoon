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

def max_check():
    i = 1
    temp = i * 2
    while temp <= left:
        if l_heap[i] > l_heap[temp] and l_heap[i]> l_heap[temp+1]:
            return
        if temp != left and l_heap[temp] < l_heap[temp+1]:
            temp += 1
        
        l_heap[temp], l_heap[i] = l_heap[i], l_heap[temp]
        
        i = temp
        temp = i * 2

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
        
def min_check():
    i = 1
    temp = i * 2
    while temp <= right:
        if r_heap[i] < r_heap[temp] and r_heap[i] < r_heap[temp+1]:
            return
                    
        if temp != right and r_heap[temp] > r_heap[temp+1]:
            temp += 1
        
        r_heap[temp], r_heap[i] = r_heap[i], r_heap[temp]
        
        i = temp
        temp = i * 2
        

def find(temp):
    global left, right, mid

    if mid <= temp:
        if left == right: # 짝수
            min_heap(temp)
        else:
            max_heap(temp)
            if l_heap[1] > r_heap[1]:
                t =r_heap[1]
                r_heap[1] = l_heap[1]
                l_heap[1] = mid
                mid = t
                min_check()
            else:
                l_heap[1], mid = mid, l_heap[1]
            
    else:
        if left == right:
            min_heap(temp)
            if left == 0 or l_heap[1] <= r_heap[1]:
                r_heap[1], mid= mid, r_heap[1]
            else:
                t = r_heap[1]
                r_heap[1] = mid
                mid = l_heap[1]
                l_heap[1] = t
                max_check()

        else:
            max_heap(temp)

    return mid

result = []
mid = int(input())
# print(mid)
result.append(mid)

for i in range(N-1):
    temp = int(input())
    result.append(find(temp))
    # print(find(temp))
print(result)