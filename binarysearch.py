myArray = [3,5,7,8,15,17,57,60,80,90]

low = 0
high = len(myArray)
mid = (low + high)//2
found = False


while found == False or (low == high):
    for i in range(high):
        searchelement = int(input("Enter a value to be searched in the array: "))
        if searchelement > myArray[mid]:
            low = (mid+1)
            for i in range (high):
                if searchelement == myArray[i]:
                    found = True
                    print("Search found at index no: ",i)
                else:
                    print("Element is not found")
        else:
            if searchelement < myArray[mid]:
                high = (mid-1)
                for i in range (high):
                    if searchelement == myArray[i]:
                        found = True
                        print("Search found at index no: ",i)
                    else:
                        print("Element is not found")
