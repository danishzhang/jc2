# DataArr = [None for i in range(7)]
# PointerArr = [None for i in range(7)]
# hPointer = 0
# sPointer = -1

# #linked list setup
# for i in range(len(PointerArr)):
#     PointerArr[i] = i + 1
    
# PointerArr[len(PointerArr)-1] = -1


# print(PointerArr)
# print(DataArr)


DataArr = [5,6,9,3, None, None, None]
PointerArr = [-1,0,1,2,5,6,-1]

spointer = 3
hpointer = 4

tempindex = spointer # spointer cannot be changed, therefore a new variable is applied to substitute the value of the spointer
while tempindex != -1: # check whether the spointer reaches -1 which is the end of the linked list
    print(DataArr[tempindex])
    tempindex = PointerArr[tempindex] # insert the value of the next index for data to be printerd from Pointer array


