class Deque:
    def __init__(self,x=-1):
        self.size = 0
        self.link = None
        self.back = None
        self.data = x
        
    def push_back(self, node):
        self.link = node
        node.back = self
    
    def push_front(self, node):
        node.link = self.link
        node.link.back = node
        self.link = node
        node.back = self
    
    def pop_back(self):
        self
        pass
        
    
head = tail = Deque()

for i in range(int(input())):
    inp = input().split()
    if inp[0] == "push_back":
        tail.push_back(Deque(int(inp[1])))
        tail = tail.link
        head.size +=1
    elif inp[0] == 'push_front':
        if head.size == 0:
            tail.push_back(Deque(int(inp[1])))
            tail = tail.link
        else:
            head.push_front(Deque(int(inp[1])))
        head.size += 1
    elif inp[0] == 'front':
        if head.size == 0:
            print(-1)
        else:
            print(head.link.data)
    elif inp[0] == 'back':
        if head.size == 0:
            print(-1)
        else:
            print(tail.data)
    elif inp[0] == 'size':
        print(head.size)
    elif inp[0] == 'empty':
        if head.size == 0:
            print(1)
        else:
            print(0)
    elif inp[0] == 'pop_back':
        if head.size ==0:
            print(-1)
        else:
            print(tail.data)
            tail = tail.back
            tail.link = None
            head.size -= 1
            
            if head.size == 0:
                tail = head
            
    elif inp[0] == 'pop_front':
        if head.size ==0:
            print(-1)
        else:
            print(head.link.data)
            if head.size == 0 or head.size == 1:
                tail = head
            else:
                head.link = head.link.link
                head.link.back = head
            head.size -= 1
