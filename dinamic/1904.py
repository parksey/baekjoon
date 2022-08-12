# N = int(input())

# def find(string, length):
#     if length > N:
#         return 0
    
#     if length == N:
#         return 1
    
#     return find(string+'1',length+1) + find(string+'00',length+2)

# one = find('1',1)
# zero = find('00',2)
# print(one+zero)

N = int(input())
n=[0 for _ in range(N)]
n[0] = 1
def solve():
    if N == 1:
        return     

    n[1] = 2

    for i in range(2,N):
        n[i] = (n[i-1] + n[i-2]) % 15746
solve()
print(n[N-1])

# N = int(input())
# n=[0 for _ in range(N+1)]

# def solve():
#     if N == 1:
#         return 1     

#     first = 1
#     second = 2

#     for i in range(3,N+1):
#         temp = second
#         second += first
#         first = temp
#     return second

# print(solve())
