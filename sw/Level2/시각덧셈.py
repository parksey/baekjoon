T = int(input())

def solve():
    time = list(map(int, input().split()))
    
    minit = time[1] + time[3]
    hour = time[0] + time[2]
    
    if minit >= 60 :
        hour += minit //60
        minit %= 60
    
    hour = hour%13+1 if hour > 12 else hour
    
    return [hour, minit]

for i in range(T):
    print("#{}".format(i+1), *solve())