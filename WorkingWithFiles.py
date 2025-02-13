# PSEUDOCODE
# OPENFILE "Numbers.txt" FOR READ/WRITE/APPEND
# READLINE "Numbers.txt", text (reading one line at a time)
# OUTPUT text (it will output the 1st data copied from Numbers.txt)
# READLINE "Numbers.txt"
# OUTPUT text (it will output the 2nd data copied from Numbers.txt)


# PYTHON
file = open("Numbers.txt", 'r') # opening the file in read mode
# text = file.read() # reads everything in the file and copies all data into one variable
# text = file.readline() # read one line at a time and store it in one variable
text = file.readlines() # read all the lines but copies the elements and forms an array of strings

total = 0
for i in range(10):
    total = total + int(text[i].rstrip()) # removing the white spaces from "ENTER" button


name = "    Shuaib    "
print(name.strip()) #removing the left and rigt white spaces
print(name.lstrip()) #removing the left white spaces
print(name.rstrip()) #removing the right wite spaces 


# How to sort the numbers from Numbers.txt into decending order
# copy the elements in the text file into an array, sort the array, then copy the element 
# back into the text file

myArr = [0 for i in range(10)] # Cambridge wants to see this to gain mark
file = open("Numbers.txt", 'r')
for i in range(10):
    text = file.readline()
    myArr[i] = text

print(myArr)
