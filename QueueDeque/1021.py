N, M = map(int,input().split())

data = list(map(int, input().split()))

count = 0

n_list = [i+1 for i in range(N)]
for d in data:
    length = len(n_list)
    index = n_list.index(d)
    
    if index < length - index:
        while n_list[0] != d:
            n_list.append(n_list[0])
            del n_list[0]
            count += 1
        del n_list[0]
    else:
        while n_list[0] != d:
            n_list.insert(0, n_list[-1])
            del n_list[-1]
            count += 1
        del n_list[0]
print(count)
    
    