K, N = map(int, input().split())

k_list = []
for i in range(K):
    k_list.append(int(input()))
    
k_list.sort()
def max_find(start, end):
    while start <= end:
        mid = (start+end)//2
        ret = 0
        for i in k_list:
            ret += i // mid
        if ret >= N:
            start = mid+1
        else:
            end = mid-1

    return end

print(max_find(1, k_list[-1]))