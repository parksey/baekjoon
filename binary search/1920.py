N = int(input())
n_list = list(map(int, input().split()))

n_list.sort()

M = int(input())
m_list = list(map(int, input().split()))

def find(start, end, m, n_list):
    if start > end:
        return 0
    elif start == end:
        return 1 if n_list[start] == m else 0
    
    mid = (start + end)//2
        
    if m == n_list[mid]:
        return 1
    if m > n_list[mid]:
        return find(mid+1,end, m, n_list)
    else:
        return find(start,mid, m, n_list)
    
for m in m_list:
    if n_list[N-1] < m:
        print(0)
    else:
        print(find(0,N-1, m, n_list))

# N = int(input())
# n_list = list(map(int, input().split()))

# n_list.sort()

# M = int(input())
# m_list = list(map(int, input().split()))

# def find(start, end, m, n_list):
#     if n_list[end] < m:
#         return 0
    
#     while start <= end:
#         mid = (start+end)//2
#         if start == end:
#             if m != n_list[mid]:
#                 return 0
#             else:
#                 return 1
#         elif  m == n_list[mid]:
#             return 1
#         elif m > n_list[mid]:
#             start = mid +1
#         else:
#             end = mid
        
#     return 0

# for m in m_list:
#     print(find(0,N-1, m, n_list))