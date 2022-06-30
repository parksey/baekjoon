class Node:
    def __init__(self, x=-1):
        self.data = x
        self.link = None
        self.size = 0
    
    def push(self, next_node):
        self.link = next_node
        
head = tail = Node()
for i in range(1, int(input())+1):
    tail.push(Node(i))
    tail = tail.link
    head.size += 1

step = False
while head.size != 1:
    step = not step
    if step:
        head.link = head.link.link
        head.size -= 1
    else:
        tail.link = head.link
        head.link = head.link.link
        tail = tail.link
        tail.link = None

print(head.link.data)