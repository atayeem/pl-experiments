def c(stack):
    size = int(stack.pop())
    if size > len(stack):
        raise ValueError(f"Tried to copy {size} elements of stack, though there are only {len(stack)} elements.")
    
    stack += stack[-size:]

def o(stack):
    if (len(stack) == 0):
        raise ValueError("Tried to print empty stack.")

    print(stack.pop(), end="")

def plus(stack):
    stack.append(stack.pop() + stack.pop())

def minus(stack):
    stack.append(stack.pop() - stack.pop())

def times(stack):
    stack.append(stack.pop() * stack.pop())

def divide(stack):
    stack.append(stack.pop() / stack.pop())

def modulo(stack):
    stack.append(stack.pop() % stack.pop())

def equals(stack):
    stack.append(stack.pop() == stack.pop())

def lessthan(stack):
    stack.append(stack.pop() < stack.pop())

def greaterthan(stack):
    stack.append(stack.pop() > stack.pop())

def _and(stack):
    stack.append(stack.pop() and stack.pop())

def _or(stack):
    stack.append(stack.pop() or stack.pop())

def _xor(stack):
    stack.append(stack.pop() ^ stack.pop())

def _not(stack):
    stack.append(not stack.pop())

def _get(stack):
    select = stack.pop()
    if select == 0:
        stack.append(str(input()))
    if select == 1:
        stack.append(int(input()))
    if select == 2:
        stack.append(float(input()))

def _grab(stack):
    stack.append(stack[-int(stack.pop())])

def _delete(stack):
    rep = stack.pop()
    for _ in range(rep):
        stack.pop()
    
keywords = {
    "c": c,
    "o": o,
    "+": plus,
    "-": minus,
    "*": times,
    "/": divide,
    "%": modulo,
    "=": equals,
    "<": lessthan,
    ">": greaterthan,
    "&": _and,
    "|": _or,
    "^": _xor,
    "!": _not,
    "g": _get,
    "G": _grab,
    "d": _delete,
    "~": lambda stack: stack.append(-stack.pop()),
    "N": lambda stack: None,
    "D": lambda stack: print(stack)
}


