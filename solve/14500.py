
shapes = [
    # -
    [
        [[0,0],[0,1],[0,2],[0,3]], # -
        [[0,0],[1,0],[2,0],[3,0]]  # | 
    ], 
    # ㅁ
    [
        [[0,0],[0,1],[1,0],[1,1]] # ㅁ
    ],
    # L
    [
        [[0,0],[1,0],[2,0],[2,1]], # L      5
        [[1,0],[1,1],[1,2],[0,2]], # ___|   2
        [[0,0],[0,1],[1,1],[2,1]], # ㄱ 
        [[0,0],[1,0],[0,1],[0,2]] # |---     1
    ],   
    # _|
    [
        [[2,0],[2,1],[1,1],[0,1]], # _|     6
        [[0,0],[0,1],[0,2],[1,2]], # ㅡㄱ    4
        [[0,0],[1,0],[2,0],[0,1]], # r       7
        [[0,0],[1,0],[1,1],[1,2]] # ㄴㅡ     3
    ] ,
    # ㄴㄱ
    [
        [[0,0],[1,0],[1,1],[2,1]],
        [[1,0],[1,1],[0,1],[0,2]]
    ],
    #r-|
    [
         [[2,0],[1,0],[1,1],[0,1]],
        [[0,0],[0,1],[1,1],[1,2]]
    ],
    # ㅜ
    [
        [[0,0],[0,1],[0,2],[1,1]], # ㅜ
        [[0,0],[1,0],[2,0],[1,1]], # ㅏ
        [[1,0],[1,1],[1,2],[0,1]], # ㅗ
        [[1,0],[0,1],[1,1],[2,1]] # ㅓ
    ]
]

N, M = map(int, input().split())

scoreMap = []
for i in range(N):
    scoreMap.append(list(map(int, input().split())))

allSum = 0

def isOutOfRange(y,x):
    return y >= N or y < 0 or x >= M or x < 0

def calc(location, startY, startX):
    global allSum
    #print(location)
    eachSum = 0
    for loc in location:
        y = loc[0] + startY
        x = loc[1] + startX
        
        if isOutOfRange(y,x):
            return
        eachSum += scoreMap[y][x]
    
    allSum = max(allSum, eachSum)
    
        
        

def find(startY, startX):
    for shape in shapes:
        for types in shape:
            calc(types, startY, startX)

def start():
    for i in range(N):
        for j in range(M):
            find(i,j)
start()
print(allSum)