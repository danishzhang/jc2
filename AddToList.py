Ldata = [None for i in range(5)]
Lpointer = [1,2,3,4,-1]

spointer = -1
hpointer = 0


def addToList(item):
    global spointer
    global hpointer
    global temp
   
    if hpointer == -1:
        print("Linked list is full")
    else:    
        temp = spointer 
        spointer = hpointer
        Ldata[spointer] = item
        hpointer = Lpointer[hpointer]
        Lpointer[spointer] = temp



item = int(input("Input an item: "))
addToList(item)
print(Ldata)
print(Lpointer)

item = int(input("Input an item: "))
addToList(item)
print(Ldata)
print(Lpointer)

item = int(input("Input an item: "))
addToList(item)
print(Ldata)
print(Lpointer)

item = int(input("Input an item: "))
addToList(item)
print(Ldata)
print(Lpointer)

