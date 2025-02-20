# 2a
arrayData = [10,5,6,7,1,12,13,15,21,8]

# 2(b)(i)
def linearSearch(searchelement):
    while searchelement != arrayData[i]:
     for i in range(len(arrayData)):
        if searchelement == arrayData[i]:
            return True
        else:
            return False

searchelement = int(input("Enter a value to check with the array: "))

if linearSearch(searchelement) == True:
    print("The value is present in the array")
else:
    print("The value is not present in the array")
    
linearSearch(searchelement)
# 2(c)

# def bubbleSort():
#     for x in range(len(arrayData)):
#         for y in range(len(arrayData[x])):
#             if arrayData[y] > arrayData[y+1]:
#                 arrayData[y], arrayData[y+1] = arrayData[y+1], arrayData[y]
