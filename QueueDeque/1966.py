class Node:
    def __init__(self, x=-1):
        self.link = None
        self.data = x
        self.size = 0
        self.isImport = False
    
    def push(self, nextNode):
        self.link = nextNode
      
    def pop(self):
        self.link = self.link.link
        
total = int(input())


def importantIndex(head):
    index = 0
    # 1 2 3 4

    max_data = head.link.data
    h = head.link.link
    i=1
    while h:
        if max_data < h.data:
            index = i
            max_data = h.data
        h = h.link
        i += 1
    return index
    

for i in range(total):
    doc, im = map(int, input().split())   
    data = list(map(int, input().split()))
    
    head = tail = Node()
    for i,d in enumerate(data):
        tail.push(Node(d))
        tail = tail.link
        head.size += 1
        if i == im:
            tail.isImport = True
    
    count = 1
    while True:
        index = importantIndex(head)
        
        for _ in range(index):
            tail.push(head.link)
            tail = tail.link
            head.pop()
            tail.link=None
        
        if head.link.isImport:
            print(count)
            break
            
        head.pop()
        head.size -= 1
        count+=1