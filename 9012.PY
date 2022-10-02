N = int(input())

def solve(string):
    stack = []
    for c in string:
        if c == '(':
            stack.append('(')
        elif c == ')':
            if not stack:
                return "NO"
            
            if stack[-1] == '(':
                stack.pop()
    
    if stack:
        return "NO"
    
    return "YES"

for i in range(N):
    string = input()
    print(solve(string))