T = int(input())

def solve(userInput):
    length = len(userInput)
    
    for i in range(length//2+1):
        if userInput[i] != userInput[-(i+1)]:
            return 0
    return 1
    

for i in range(T):
    userInput = input()
    print("#{} {}".format(i+1, solve(userInput)))