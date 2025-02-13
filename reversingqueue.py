# reversing the queue by implemmenting stack procedure


queue = [1,2,3,4,5]
lenofcue = 5
rear = -1 
front = 0
maxsize = len(queue) +1 # maxsize needed to be len(queue) + 1 (6)


def enqueue(item):
    global lenofcue
    global rear
    global front
    if lenofcue == maxsize:
        print("the queue is full")
    elif rear == maxsize - 1:
         rear = 0
    else:
        rear = rear+1
        queue[rear] = item
        lenofcue = lenofcue + 1

def dequeue():
    global temp
    global lenofcue
    global rear
    global front
    if lenofcue - 1 == -1: # index 0 in lenofcue has a value which needs to be outputted so it cannot stop at index 0
        print("The queue is already empty, unable to remove")
    elif front == maxsize - 1:
        front = 0
    else:
        temp = queue[front]
        queue[front] = None
        front = front + 1
        lenofcue = lenofcue - 1
    return temp


stack = [None for i in range(5)] 
low = 0
top = -1

def pop():
    global top
    if top == -1:
        print("The stack is empty.")
    else:
        print("The item popped out is ",stack[top])
        stack[top] = None
        top = top - 1

def push(item):
    global top
    if top == len(stack)-1 :
        print("Stack is full")
    else:
        top = top + 1
        stack[top] = item


push(dequeue())
print(stack)
push(dequeue())
print(stack)
push(dequeue())
print(stack)
push(dequeue())
print(stack)
push(dequeue())
print(stack)

enqueue(pop())
print(queue)
enqueue(pop())
print(queue)
enqueue(pop())
print(queue)
enqueue(pop())
print(queue)
enqueue(pop())
print(queue)
