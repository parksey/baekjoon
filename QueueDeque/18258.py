import sys
class Node:
    def __init__(self, x=-1):
        self.data = x
        self.link = None
        self.backlink = None
        self.size = 0
    
    def push(self, next_node):
        self.link = next_node
        next_node.backlink = self
    
head = tail = Node()
    
for i in range(int(sys.stdin.readline())):
    input_str = sys.stdin.readline().split()
    
    if input_str[0] == 'push':
        tail.push(Node(int(input_str[1])))
        tail = tail.link
        head.size += 1
    elif input_str[0] == 'front':
        if head.link == None:
            print(-1)
        else:
            print(head.link.data)
    elif input_str[0] == 'back':
        print(tail.data)
    elif input_str[0] == 'size':
        print(head.size)
    elif input_str[0] == 'pop':
        if head.link == None:
            print(-1)
        else:
            print(head.link.data)
            head.link = head.link.link
            head.size -= 1
            if head.size == 0:
                tail = head
            
    elif input_str[0] == "empty":
        if head.size == 0:
            print(1)
        else:
            print(0)