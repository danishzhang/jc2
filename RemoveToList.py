
# check whether the array is empty before removing an elemnt (works for all : queue, stack, linked list, etc.)
# search whether the item to be deleted is found in the linked list
# if item to be deleted is found, remove the item

Ldata = [5,6,7,8,None]
Lpointer = [-1,0,1,2,-1]

spointer = 3
hpointer = 4


def DeleteFromList(item):
    global spointer
    global hpointer

    itempointer = spointer
    while Ldata[itempointer] != item and spointer != -1:
        if 