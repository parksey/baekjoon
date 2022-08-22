N = int(input())
n_list = list(map(int, input().split()))

arr = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if n_list[i] > n_list[j] and arr[i] < arr[j]+1:
            arr[i] = arr[j] + 1
print(max(arr))