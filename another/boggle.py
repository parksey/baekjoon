inp = [
    ['U','R','L','P','M'],
    ['X','P','R','E','T'],
    ['G','I','A','E','T'],
    ['X','T','N','Z','Y'],
    ['X','O','Q','R','S'],
]

inp2 = [
    ['N','N','N','N','S'],
    ['N','E','E','E','N'],
    ['N','E','Y','E','N'],
    ['N','E','E','E','N'],
    ['N','N','N','N','N']
]

dx = [-1,0,1,
      -1,0,1,
      -1,0,1]

dy = [-1,-1,-1,
      0,0,0,
      1,1,1]

def boggle(y,x, word):
    if x > 5 or x < 0 or y > 5 or y < 0:
        return False

    if inp2[y][x] not in word:
        return False
    
    for i in range(8):
        boggle(y+dy[i], x+dx[i], word)
        
boggle(0,0,"PRETTY")