


priorities = {
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '(':1
}

def infixToRPL(infix):
    stack = []
    rpl =[]
    out=[]
    for i in range(len(infix)):
        if type(infix[i])==int:
            rpl.append(infix[i])
        elif infix[i] == "+" or infix[i] == "*" or infix[i] == "/" or infix[i] == "-":
            while len(stack) > 0 and priorities[stack[-1]] >= priorities[infix[i]]:
                rpl.append(stack.pop())
            stack.append(infix[i])
        elif infix[i] == "(":
            stack.append(infix[i])
        elif infix[i] == ")":
         while len(stack) > 0:
             rpl.append(stack.pop())
    while len(stack) > 0:
        rpl.append(stack.pop())
    for i in rpl:
        if i == "(":
            pass
        else:
         out.append(i)
    return out
            
# infixToRPL([1, '*', 3, '+', 4])
print(infixToRPL(['(',1,'+', 3,'*',5,')','*', 4]))
#print(infixToRPL([1, '+', 3, '*', 4]))