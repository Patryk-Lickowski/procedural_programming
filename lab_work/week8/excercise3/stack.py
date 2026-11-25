stack = []

def push(element):
    stack.append(element)

def pop():
    if is_empty():
        return "Stack is empty"
    return stack.pop

def peek():
    if is_empty():
        return "Stack is empty"
    return stack[-1]

def is_empty():
    return len(stack) == 0

def size():
    return len(stack)
