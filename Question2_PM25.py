#2 a 
Data = [[[],[],[],[]],
        [[],[],[],[]],
        [[],[],[],[]],
        [[],[],[],[]],
        [[],[],[],[]]]

Rows = 5


#2 b
def SetUp():
    global rowVal
    rowVal = int(input("Enter the quantity of rows you would like to enter: "))
    if rowVal >= 1 and rowVal <= 5:
        print("The quantity for row is valid")
    else:
        print("The quantity is not valid, please enter a number from 1 to 5")

    
    for x in range(rowVal):
        print("This is row", x+1)
        for y in range(len(Data[x])):
            data = int(input("Enter a number: "))
            Data[x][y] = data

#2 c i
SetUp()
print(Data)


#2 d i # skip recheck later
def BubbleSort():
    for i in range(rowVal):
        for j in range(len(Data[i]-1)):
            while (Data[i][j] > Data[i][j+1]):
                Data[i][j], Data[i][j+1] = Data[i][j+1], Data[i][j]
                j += 1

# #2 d ii
BubbleSort()
print(Data)

#2 e i
def RecursiveBinarySearch(rowSearch, DataToFind, low, high): 
    lenofarray = 0
    for i in range(high - low):
        if lenofarray == len(Data[rowSearch]):
            print("Data is not found")
        else:
            if Data[i][low] != DataToFind:
                lenofarray += 1
            else:
                print("Data is found in row ", rowSearch, " at column ", i)
                
#2 e ii

    
        

