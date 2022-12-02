
def evaluate(rpl):
    stack=[]
    #for elem in rpl:
    for i in range(len(rpl)):
        
        #if rpl[i] != "+" and rpl[i] != "*" and rpl[i] != "/" and rpl[i] != "-":
        if type(rpl[i]) ==int:
            stack.append(rpl[i])
        elif rpl[i] == "+":
            #if len(stack) == 2:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif rpl[i] == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        elif rpl[i] == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(a//b)
        elif rpl[i] == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(a-b)
            
    return stack.pop()
            
            
rpl = [1,2,"+",3,"*"]
print(evaluate(rpl))