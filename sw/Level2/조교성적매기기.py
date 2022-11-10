T = int(input())

grade = ["D0", "C-", "C0", "C+", "B-", "B0", "B+", "A-", 'A0', "A+"]

def calc(m,e,x):
    return m*0.35 + e*0.45+x*0.2

def solve():
    N, K = map(int, input().split())
    
    stuScore = []
    
    for i in range(N):
        m,e,x = map(int, input().split())
        stuScore.append([calc(m,e,x)])
        
    temp = sorted(stuScore, key = lambda x: x[0])
    ratio = N // 10
    
    for i in range(N):
        temp[i].append(grade[i//ratio])

    return stuScore[K-1][1]


for i in range(T):
    print("#{} {}".format(i+1, solve()))
