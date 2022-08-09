sudoku = []
need = []
for i in range(9):
    temp = list(map(int, input().split()))
    for j in range(9):
        if temp[j] == 0:
            need.append([i,j])
    sudoku.append(temp)

def isIn(loc):
    isAble = [0] * 9
    r_y = loc[0] // 3 * 3
    r_x = loc[1] // 3 * 3

    for i in range(9):
        row = sudoku[loc[0]][i]
        col = sudoku[i][loc[1]]
        round = sudoku[r_y + i//3][r_x+i%3]
        if row != 0:
            isAble[row-1] = 1
        if col != 0:
            isAble[col-1] = 1
        if round != 0:
            isAble[round-1] = 1
        
    re = []
    for i in range(9):
        if isAble[i] == 0:
            re.append(i+1)
    return re

def printSudoku():
    for i in sudoku:
        print(' '.join(list(map(str, i))))

needSize=len(need)   
def check(index):
    if index == needSize:
        return False
    
    haveTo= isIn(need[index])
    
    if len(haveTo)==1 and index == needSize-1:
        sudoku[need[index][0]][need[index][1]] = haveTo[0]
        printSudoku()
        return True
    
    for data in haveTo:
        sudoku[need[index][0]][need[index][1]] = data
        if check(index+1):
            return True
        sudoku[need[index][0]][need[index][1]] = 0


check(0)
