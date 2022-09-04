a = [
    [6],
    [1,2],
    [3,7,4],
    [9,4,1,7],
    [2,7,5,9,4]
]

b = [
    [1],
    [2,4],
    [8,16,8],
    [32,64,32,64],
    [128,256,128,256,128]
]

def find(n):
    n_list = [[0]*i for i in range(1,6)]
    
    n_list[0][0] = n[0][0]
    
    for i in range(1,5):
        n_list[i][0] = n_list[i-1][0] + n[i][0]
        n_list[i][i] = n_list[i-1][i-1] + n[i][i]

        for j in range(1,i):
            n_list[i][j] = n[i][j] + max(n_list[i-1][j-1], n_list[i-1][j])

    return max(n_list[-1])    
print(find(a))