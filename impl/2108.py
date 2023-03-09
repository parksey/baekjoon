N = int(input())
result = [0 for _ in range(8001)]

mean = 0

mid_data = 0
mid_index = 0
mid = N//2

many = 0
many_index = 0
check = False

low = high = -1

for i in range(N):
    a = int(input())
    mean += a
    result[a+4000] += 1

for index, data in enumerate(result):
    if data != 0:
        if mid_index <= mid and mid_index + data >= mid:
            mid_data = index
        mid_index += data
        
        if low == -1:
            low = index
        high = index
        
        if many == data and not check:
            check = True
            many_index = index
        elif many < data: 
            check = False
            many = data
            many_index = index
if N == 0:
    print("0\n0\n0\n1")
else:
    print(round(mean/N))
    print(mid_data-4000)
    print(many_index-4000)
    print(high - low)