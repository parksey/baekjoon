# # 8
# # 1 8
# # 3 9
# # 2 2
# # 4 1
# # 6 4
# # 10 10
# # 9 7
# # 7 6

# N = int(input())

# li = []
# for i in range(N):
#     li.append(list(map(int, input().split())))
# li.sort(key=lambda x: x[0])
# print(li)

# def solution(citations):
#     answer = 0
#     citations.sort()

#     length = len(citations)
#     start = 0
#     end = length-1
#     ind = 0
#     while True:
#         if ind == 10:
#             break
#         ind+=1
#         mid = (start+end)//2
#         h =(length-mid)
#         if citations[mid] >= h:
#             if mid == 0:
#                 answer = h
#                 break
#             if citations[mid-1] <= h:
#                 answer = h
#                 break
#             else:
#                 end = mid
#         else:
#             start = mid
#     return answer

#     # 3 5 5 6 7 7 8   5
#     # 0 1 2 3 4 5 6
#     # 7 6 5 4 3 2 1
# print(solution([2,2,2,2,2]))

# def make(scoville, heap, h_index):
#     for data in scoville:
#         h_index+=1
#         push(heap, h_index, data)
#     return h_index

# def push(heap, h_index, data):
#     cmp = 2
#     index = h_index
#     heap[index] = data
#     while index>1:
#         iDiv2 = index // 2
#         if heap[iDiv2] > heap[index]:
#             heap[index], heap[iDiv2] = heap[iDiv2], heap[index]
#         index = iDiv2
        
# def pop(heap,h_index):
#     index = 1
#     next = 2
#     reData = heap[1]
#     heap[1] = heap[h_index+1]
#     heap[h_index+1] = 0
#     while next<=h_index:
#         if next == h_index:
#             if heap[next] > heap[index]:
#                 return reData
#         else:
#             if heap[next] > heap[index] and heap[next+1] > heap[index]:
#                 return reData

#             if heap[next] > heap[next+1]:
#                 next += 1
#         heap[next], heap[index] = heap[index], heap[next]

#         index = next
#         next *= 2

#     return reData
                
