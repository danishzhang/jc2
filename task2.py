#Find the total of all the element for each row in a 2D array
#Find the total of all the elements for each column in 2D array
#Find the highest in each row of a 2D array
#Find the highest in each column of a 2D array

Array = [[4, 5, 8], 
         [8, 4, 2], 
         [9, 1, 5]]

for row in range(len(Array)): # row = 0
    sum = 0
    for col in range(len(Array[row])):
        sum = sum + Array[row][col]
    print("Sum of row ", row +1, "is ", sum)

