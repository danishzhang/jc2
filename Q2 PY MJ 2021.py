# 2(a)
arrayData = [10,5,6,7,1,12,13,15,21,8]

# def linearSearch(searchelement):
#     for i in range(len(arrayData)):
#         if searchelement == arrayData[i]:
#             return True

# searchelement = int(input("Enter a value to check with the array: "))

# if linearSearch(searchelement):
#     print("The value is present in the array")
# else:
#     print("The value is not present in the array")
        
# 2(c)

def bubbleSort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData[x])):
            if arrayData[y] > arrayData[y+1]:
                arrayData[y], arrayData[y+1] = arrayData[y+1], arrayData[y]






