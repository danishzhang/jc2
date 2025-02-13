#initialising a stack

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

