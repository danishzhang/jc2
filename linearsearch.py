#LinearSearch.py

Array = [2,3,4,7,8,5,9,0,1,6]
search = int(input("Enter a value to be compared: "))  
found = False

for i in range(10):
    if search == Array[i]:
        found = True

if found :
    print("The element is found in the array")
else :
    print("The element is not found in the array")