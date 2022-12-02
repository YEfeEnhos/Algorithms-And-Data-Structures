def convert(array):
    stack=[]
    skiped=0
    arr = [2,8,"*",6,"+"] 

    for i in range(len(array)):
        if type(array[i]) == int:
         if len(stack)>2:
            stack.append(array[i])
         elif len(stack)<2 and skiped == 0:
            stack.append(array[i])
         elif len(stack)<2 and skiped != 0:
             stack.append(skiped)
             stack.append(array[i])
             skiped=0
        elif array[i] == "*":
            if len(stack)>2:
             if type(stack[i-1]) == int and type(stack[i-2]) == int:
                 stack.append(array[i])
             else:
                 skiped=array[i]
            else:
                 skiped=array[i]
                 
        elif array[i] == "+":
            if len(stack)>2:
             if type(stack[i-1]) == int and type(stack[i-2]) == int:
                 stack.append(array[i])
             else:
                 skiped=array[i]
            else:
                 skiped=array[i]
    
    
    return arr

    


array = [2,"*",8,"+",6]
print(convert(array))