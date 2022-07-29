N = int(input())

heap = [0 for _ in range(N+1)]

def update():
    i = index
    while i >= 2:
        temp = i // 2
        if heap[temp] < heap[i]:
            heap[temp], heap[i] = heap[i], heap[temp]
        else:
            return
        i = temp
    
    
def delete():
    i = 1
    temp = i * 2
    while temp < index:
        if heap[i] > heap[temp] and heap[i]> heap[temp+1]:
            return
        if heap[temp] < heap[temp+1]:
            temp += 1
        
        heap[temp], heap[i] = heap[i], heap[temp]
        
        i = temp
        temp = i * 2
        
result = []
index = 0
for i in range(N):
    temp = int(input())
    if temp == 0:
        if index == 0:
            result.append(0)
        else:
            result.append(heap[1])
            heap[1] = heap[index]
            delete()
            heap[index] = 0
            index -= 1
    else:
        index += 1
        heap[index] = temp
        update()

for i in result:
    print(i)
