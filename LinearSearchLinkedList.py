# Search an element from the linked list

Llist = [1,5,7,8,9]
Lpointer = [-1,0,1,2,3]

spointer = 4
hpointer = 5
found = False

temp = spointer
def search(item):
    global temp
    global found
    while  temp != -1:
       if item == Llist[temp]:
           return item
       else:
           temp = Lpointer[temp]
    return -1 

item = int(input("Enter a value to be searched: "))
print(search(item))


# if item == Llist[temp]:
#     print("The value is found in the array at pointer", temp)
# else:
#     print("Value is not found in the array")

