N = int(input())

n_list=list(map(int, input().split()))

left = [1 for i in range(N)]
right = [1 for i in range(N)]

def find():
    for i in range(N):
        for j in range(i):
            if n_list[i] > n_list[j] and left[i] < left[j]+1:
                left[i] = left[j] + 1
            if n_list[N-1-i] > n_list[N-1-j] and right[N-1-i] < right[N-1-j]+1:
                right[N-1-i] = right[N-1-j]+1

find()
l_max = max(left)
index = left.index(l_max)

if index == N-1:
    print(l_max)
elif l_max == 0:
    print(max(right))
else:
    r_max = 0
    for i in right[index+1:]:
        if r_max < i and i <l_max:
            r_max= i
    print(l_max+r_max)