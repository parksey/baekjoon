# def solve(string):
#     stack = []
#     for c in string:
#         if c == '(' or c == '[':
#             stack.append(c)
#         elif c == ')':
#             if not stack or stack[-1] == '[':
#                 return "no"
            
#             if stack[-1] == '(':
#                 stack.pop()
#         elif c == ']':
#             if not stack or stack[-1] == '(':
#                 return "no"
            
#             if stack[-1] == '[':
#                 stack.pop()
#     if stack:
#         return "no"    
#     return "yes"
        


# while True:
#     string = input()
#     if string == ".":
#         break
    
#     print(solve(string))

f2f = {'(': ')', '[': ']'}

def solve(string):
    stack = []
    for c in string:
        if c in f2f.keys():     # '(', '[' 일때
            stack.append(c)
        elif c in f2f.values(): # ')', ']' 일때
            if not stack or c != f2f[stack[-1]]:
                return "no"
                
            stack.pop()
    if stack:
        return "no"
    return "yes"
while True:
    string = input()
    if string == ".":
        break

    print(solve(string))