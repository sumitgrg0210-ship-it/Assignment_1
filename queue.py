# Creating queue
queue = []

# Enqueue function (add element)
def enqueue(item):
    queue.append(item)
    print(item, "added to queue")

# Dequeue function (remove element)
def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print(queue.pop(0), "removed from queue")

# Display function
def display():
    print("Queue elements:", queue)

# Operations
enqueue(10)
enqueue(20)
enqueue(30)

display()

dequeue()
display()