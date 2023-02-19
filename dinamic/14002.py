N = int(input())

dataList = list(map(int, input().split()))

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

    def setPrev(self, node):
        self.prev = node

def solve():
    dp = [[1, Node(dataList[i])] for i in range(N)]
    
    for i in range(1, N):
        for j in range(i):
            if dataList[i] <= dataList[j]:
                continue
            
            if dp[i][0] < dp[j][0] +1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1].setPrev(dp[j][1])
    
    
    
    return max(dp, key=lambda x: x[0])

def makeList(maxNode):
    printList = []
    while maxNode.prev:
        printList.append(maxNode.data)
        maxNode = maxNode.prev
    printList.append(maxNode.data)
    return printList[::-1]

maxData, maxNode = solve()


print(maxData)
print(*makeList(maxNode))