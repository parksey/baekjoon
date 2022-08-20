N = int(input())

number = [1 for i in range(10)]
number[0]=0

for i in range(1,N):
    last_stair = number.copy()
    for j in range(10):
        if j == 0:
            number[j]=last_stair[j+1] % 1000000000
        elif j == 9:
            number[j]=last_stair[j-1] % 1000000000
        else:
            number[j]=(last_stair[j-1]+last_stair[j+1]) % 1000000000

print(sum(number)% 1000000000)