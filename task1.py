#Find the total of all the elements in the array
#Find the highest and lowest elements

Array = [2,4,6,8,10]

print("There are a total of: ", len(Array)," elements in the array.")
highest = Array[0]
lowest = Array[0]

for i in range(len(Array)):
    if Array[i] > highest:
        highest = Array[i]
    if Array[i] < lowest:
        lowest = Array[i]

print("The highest element in the array is: ",highest)
print("The lowest element in the array is: ", lowest)