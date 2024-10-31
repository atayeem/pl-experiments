from process import *
from keywords import * 
from types import FunctionType as function


def execute(func, stack=None):
    if type(func) is function:
        return func(stack)

    elif type(func) in (int, float, str, bool):
        func = [func]

    if not stack:
        stack = []

    for token in func:
        if type(token) in (int, float, list, bool):
            stack.append(token)
        
        # String literals
        if type(token) is tuple:
            stack.append(token[0])

        if type(token) is str:
            if token[0] == ".":
                # Expand function pointer
                stack.append(keywords[token[1]])
            
            elif token[0] == "$":
                # Reusable variable assignment
                keywords[token[1]] = stack.pop()

            elif token in keywords:
                # Call function
                execute(keywords[token], stack)
            
            else:
                # Create new function
                keywords[token] = stack.pop()
    
    return stack

def _if(stack):
    cond = stack.pop()
    exp1 = stack.pop()
    exp2 = stack.pop()
    if (bool(cond)):
        execute(exp1, stack)
    else:
        execute(exp2, stack)

def _repeat(stack):
    repetitions = stack.pop()
    func = stack.pop()
    if int(repetitions) == -1:
        while True:
            execute(func, stack)
    
    for _ in range(int(repetitions)):
        execute(func, stack)

keywords["i"] = _if
keywords["r"] = _repeat

def main():
    file = open(input("Input file: "), "r")
    text = file.read()

    program = process(text)
    print(program)
    execute(program)

    file.close()

if __name__ == "__main__":
    main()

