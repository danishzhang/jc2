# num1 = int(input("Enter the first value: "))
# num2 = int(input("Enter the second value: "))

# Exception Handling (Do this everytime for files regardless whether the question specify or not)
# try:
#     print("The Result: ", num1/num2)
# except ZeroDivisionError: # This is the specific error in the division case which is appreciated by cambridge
#     print(f"{num1} cannot be divided by {num2}")


#(Do this everytime for files regardless whether the question specify or not)
try:
    file = open("Karel.txt",'r')
except FileNotFoundError:
    print("The file you are trying to open does not exist")
finally:
    file.close()