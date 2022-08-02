T = int(input())

def length(temp, n):
    x = temp[0] - n[0]
    y = temp[1] - n[1]
    return x**2 + y**2
    

def find(start, end, n):
    start_length = length(start, n)
    end_length = length(end, n)
    
    n2 = n[2]**2
    if n2 > start_length and n2 > end_length:
        return 0
    
    if n2 <= start_length and n2 <= end_length:
        return 0
    
    return 1
    
for i in range(T):
    t =list(map(int, input().split()))
    start = t[:2]
    end = t[2:]
    count = 0
    N = int(input())
    for j in range(N):
        n = list(map(int , input().split()))
        count += find(start, end, n)
    print(count)
    