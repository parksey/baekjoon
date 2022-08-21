N = int(input())

n_list = [0 for i in range(N)]

for i in range(N):
    n_list[i] = int(input())

result = [0 for i in range(N)]

def find():
    result[0] = n_list[0]
    if N == 1:
        return result[0]

    result[1] = n_list[1] +n_list[0]
    if N == 2:
        return result[1]
    
    result[2] = max(n_list[0] +n_list[1], n_list[0] + n_list[2], n_list[1] +n_list[2])
    for i in range(3,N):
        result[i] = max(result[i-1], n_list[i]+ result[i-2], n_list[i]+n_list[i-1]+result[i-3])

find()
print(result[-1])