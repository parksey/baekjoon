#  시간 초과
# N = int(input())
# n_list = list(map(int, input().split()))

# n_list.sort()

# M = int(input())
# m_list = list(map(int, input().split()))

# def add(mid,m):
#     left = mid
#     right = mid +1
#     ret = 0
    
#     l_done = False
#     r_done = False
    
#     while not l_done or not r_done:
#         if left > -1 and n_list[left] == m:
#             ret += 1      
#             left -= 1
#         else:
#             l_done = True
#         if right < N and n_list[right] == m:
#             ret += 1
#             right += 1
#         else:
#             r_done = True
#     return ret

# def find(start, end, m):
#     if start > end:
#         return 0
#     elif start == end:
#         if n_list[start] == m:
#             return add(start,m)
#         else:
#             return 0

#     mid = (start + end) // 2  
#     if n_list[mid] == m:
#         return add(mid,m)
#     elif n_list[mid] < m:
#         return find(mid+1, end, m)
#     else:
#         return find(start, mid, m)
    
# for m in m_list:
#     print(find(0,N-1,m))

N = int(input())
n_list = list(map(int, input().split()))

n_list.sort()
count_list = {}
tmp = n_list[0]-1
for i in n_list:
    if tmp != i:
        count_list[i] = 1
        tmp = i
    else:
        count_list[i] += 1

M = int(input())
m_list = list(map(int, input().split()))

def find(start, end, m):
    if start > end:
        return False
    elif start == end:
        if n_list[start] == m:
            return True
        else:
            return False

    mid = (start + end) // 2  
    if n_list[mid] == m:
        return True
    elif n_list[mid] < m:
        return find(mid+1, end, m)
    else:
        return find(start, mid, m)
    
for m in m_list:
    if find(0,N-1,m):
        print(count_list[m], end=" ")
    else:
        print(0, end=" ")
