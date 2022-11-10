T = int(input())

def solve(N):
    numberList = [i for i in range(1,N+1)]

    return sum(numberList[::2]) - sum(numberList[1::2])

for i in range(T):
    N = int(input())

    print("#{} {}".format(i+1, solve(N)))