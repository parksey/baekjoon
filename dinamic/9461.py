N = int(input())

n = [0 for i in range(100)]
n[0]=n[1]=n[2] = 1
n[3] =n[4] = 2

for loop in range(N):
    case = int(input())
    if n[case-1] !=0:
        print(n[case-1])
        continue
    
    for i in range(5, case):
        n[i] = n[i-1]+n[i-5]
    print(n[case-1])