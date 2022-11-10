T = int(input())

def solve():
    return sorted(list(map(int, input().split())))

for i in range(T):
    input()
    print("#{}".format(i+1), *solve())