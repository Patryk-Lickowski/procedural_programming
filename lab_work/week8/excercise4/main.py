import queue_def

queue_def.enqueue('Alice')
queue_def.enqueue('Bob')
queue_def.enqueue('Charlie')
queue_def.enqueue('Diana')

next_customer = queue_def.peek()

print(f"\nThe queue is: {queue_def.queue}\nThe next customer is: {next_customer}\n")

for i in range(queue_def.size()):
    print(f"\n{queue_def.dequeue()} has been served")

print("\nThe queue is empty\n")
