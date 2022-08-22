# 8
# 1 8
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6


# 1 2 3 4 5 6 7 8 9 10
# 5 2 4 3 0 2 2 0 2 0

# 0 1 0 3 0 2 2 0 2 0
N = int(input())

result = {}
index = {}
for i in range(N):
    A,B = map(int, input().split())
    
    for k,v in result.items():
        print(k,v[0])
        if (k < A and v[0] > B) or (k > A and v[0] < B):
            result[k].append(A)
            index[k] +=1
    result[A] = [B]
    index[A] = 0
    
print(result)
print(index)