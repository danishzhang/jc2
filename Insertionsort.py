#Insertion Sort

Arr = [4,7,9,1,3,2]
for i in range(1, len(Arr)): # i is from range of 1 to length of Array
    j = i-1
    key = Arr[i]
    while (key < Arr[j] and j>= 0): # key is compared to Arr[j] and j must be more than 0 
        Arr[j], Arr[j+1] = Arr[j+1], Arr[j] # e.g 2,3 = 3,2 (faster method for swapping)
        j = j - 1 # j decremented by 1 to check key with values from previous index

print (Arr)
