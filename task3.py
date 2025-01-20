#1) Input a search value output the row number and the column number where the element is present
#or and appropriate message if the element is not present

Array = [[4, 5, 8], 
         [8, 4, 2], 
         [9, 1, 6]]
found = False
search = int(input("Input an element that you would want to search: "))
for row in range(len(Array)):
    for col in range(len(Array[row])) or found == False:
        if search == Array[row][col]:
            found = True
            posRow = row + 1
            posCol = col + 1
        else: 
            found = False

if found == True:
    print("The search element is found in row ",posRow," and column ",posCol)
else:
    print("The search element is not found")

#2) Input a search value and the row number to search for and output the column number where the
#element is present or an appropriate message if the element is not present

#3) SOrt each row of the 2D array using Bubble Sort and then input a search value and the row number
#to search for and output the column number where the element is present or an appropriate message
#if the element is not present using BINARY SEARCH
