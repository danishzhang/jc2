# BinaryTree = [[-1, i+1 , -1] for i in range(10)]

# BinaryTree[9] = [-1,-1,-1]

# print(BinaryTree)

Tree = [[1,9,2],
        [3,7,-1],
        [4,13,5],
        [-1,5,-1],
        [-1,12,-1],
        [-1,15,-1],
        [-1,7,-1],
        [-1,8,-1],
        [-1,9,-1],
        [-1,-1,-1]]

f_pointer = 0
r_pointer = 6

def SearchTree(item):
    global itempointer
    itempointer = rPointer
    while Tree[itempointer][1] != item and itempointer != -1:
        if item < Tree[itempointer][1]:
            itempointer = Tree[itempointer][0] 
        else:
            itempointer = Tree[itempointer][2]
    return itempointer
# num1 = int(input("Enter the first number: "))
item = int(input("Please enter a value to be searched: "))

if SearchTree(item) != -1:
    print(f"The value is found on index {itempointer}")
else:
    print("Item is not found in the Tree")

def Insertion():
    global f_pointer
    global r_pointer

    if f_pointer != -1:
        print("Binar tree is already full")
    else:
        new_pointer = f_pointer
        f_pointer = Tree[new_pointer][1]

        if r_pointer == -1:
            r_pointer = new_pointer
        else:
            itempointer = r_pointer
            while itempointer != -1:
                
        

# if freepointer is pointing to 0, the new item pointer will be our new rootpointer.