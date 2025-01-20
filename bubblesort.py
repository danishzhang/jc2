#Bubble sort 

Array = [12,11,8,7,1]
print(Array)

swap = True
Pass = 1

while swap == True or Pass < len(Array):
    swap = False
    for i in range(len(Array)-1):
        if Array[i] > Array[i+1]:
            temp = Array[i]
            Array[i] = Array[i+1]
            Array[i+1] = temp
            swap = True 
    Pass = Pass + 1
    

print(Array)