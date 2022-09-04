A = input()
B = input()

lenA = len(A)
lenB = len(B)

dp = [[0]*lenB for i in range(lenA)]

def find(a,b):
    dp[0][0] = 1 if (A[0]==B[0]) else 0
    for i in range(1,lenB):
        dp[0][i] = 1 if A[0] == B[i] else dp[0][i-1] 
    for i in range(1,lenA):
        dp[i][0] = 1 if A[i] == B[0] else dp[i-1][0]
    
    for i in range(1,lenA):
        for j in range(1,lenB):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
find(A,B)
print(dp[lenA-1][lenB-1])