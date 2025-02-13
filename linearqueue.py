# initialising a queue
array = [None for i in range(5)]
lenofcue =  0
rear = -1 
front = 0
maxsize = len(array) 

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
        array[rear] = item
        lenofcue = lenofcue + 1

def dequeue():
    global lenofcue
    global rear
    global front
    if lenofcue == 0:
        print("The queue is already empty, unable to remove")
    elif front == maxsize - 1:
        front = 0
    else:
        array[front] = None
        front = front + 1
        lenofcue = lenofcue - 1

item = int(input("Input an item: "))



print()
