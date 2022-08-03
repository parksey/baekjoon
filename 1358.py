W, H, X, Y, P = map(int, input().split())

count = 0

def length(x,y,xr,yr,r):
    delta_x = (xr-x)**2
    delta_y = (yr-y)**2
    
    if delta_x + delta_y < r**2:
        return True
    return False

def isIn(x,y):
    r = H/2
    if y < Y or y > Y+H:
        return False
    
    if x > X-r and x < X:
        return length(x,y,X,Y+r,r)

    if x >= X and x < X+W:
        return True
    
    if x>= X+W and x < X+W+r:
        return length(x,y,X+W,Y+r,r)
    
    return False
                
    
    
        
    
for i in range(P):
    x,y = map(int,input().split())
    if isIn(x, y):
        count +=1
    
print(count)