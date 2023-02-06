'''
1 0 1 0 1 1 1 1
0 1 2 3 4 5 6 7
'''

gear = [input() for i in range(4)]

th = 2
nh = 6

K = int(input())

def change(num, direction):
    if direction == 1:
        gear[num] = gear[num][-1] + gear[num][:-1]
    else:
        gear[num] = gear[num][1:] + gear[num][0]




def rightRotate(num, direction):
    if num < 0:
        return

    if gear[num][th] == gear[num+1][nh]:
        return
        
    rightRotate(num-1, direction * -1)
    change(num, direction)

def leftRotate(num, direction):
    if num > 3:
        return
    
    if gear[num][nh] == gear[num-1][th]:
        return
    
    leftRotate(num+1, direction * -1)
    change(num, direction)

def solve():
    gearNumber, direction = map(int, input().split())
    
    rightRotate(gearNumber-2, direction*-1)
    leftRotate(gearNumber, direction*-1)
    change(gearNumber-1, direction)

for i in range(K):
    solve()

addNumber = 1
result = 0
for g in gear:
    if g[0] == '1':
        result += addNumber
    addNumber*=2
print(result)