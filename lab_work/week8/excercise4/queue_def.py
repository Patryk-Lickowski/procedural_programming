queue = []

def enqueue(customer):
    queue.append(customer)

def dequeue():
    if is_empty():
        return 'The queue is currently empty'
    return queue.pop(0)

def peek():
    if is_empty():
        return 'The queue is currently empty'
    return queue[0]

def is_empty():
    return len(queue) == 0

def size():
    return len(queue)
