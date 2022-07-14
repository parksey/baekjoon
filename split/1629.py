A, B, C = map(int, input().split())

def split(A, b):
    if b==1:
        return A

    temp = split(A, b//2) % C
    temp *= temp
    if b % 2 == 1:
        temp *= A%C 
    
    return temp

print(split(A, B) % C)