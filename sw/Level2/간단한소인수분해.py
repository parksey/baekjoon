T = int(input())

NUMBER = [2,3,5,7,11]

def solve():
    N = int(input())
    ret = [0]*len(NUMBER)
    for i in range(len(NUMBER)):
        cnt = 0
        while N % NUMBER[i] == 0:
            N //= NUMBER[i]
            cnt+=1

        ret[i] = cnt
    return ret

for i in range(T):
    print("#{}".format(i+1), *solve())