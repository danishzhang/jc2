# Q1a
class Employee:
    def __init__(self, Name, EmployeeID, Department):
        self.__Name = Name
        self.__EmployeeID = EmployeeID
        self.__Department = Department

# Q1b
    def GetName(self):
        return self.__Name
    def GetEmployeeID(self):
        return self.__EmployeeID
    def GetDepartment(self):
        return self.__Department
    
# Q1c
    def ChangeDepartment(self,NewDepartment):
        self.__Department = NewDepartment

# Q1d
AllEmployees = [Employee("",0,"") for i in range(10)]
def ReadData():
    index = 0
    file = open('C:/Users/danis/Desktop/cs/JC2/PYP/Checkpoint Assessment/Employees.txt','r') # if file cannot be read copy the file path from file explorer and change \ into /
    tempName = file.readline().strip()
    while tempName != "":
       tempEmployeeID = file.readline().strip()
       tempDepartement = file.readline().strip()
       AllEmployees[index] = Employee(tempName, tempEmployeeID, tempDepartement)
       index += 1
       tempName = file.readline().strip()
ReadData()
print(AllEmployees[0].GetName())

# Q1e
EmployeeName = input("Enter an Employee Name to be searched: ")
found = False
while found == False and i < len(AllEmployees):
    if AllEmployees[i].GetName() == EmployeeName:
        tempIndex = AllEmployees[i].GetEmployeeID()
        found = True
    i += 1
if found == True:
    print("Employee name is found. The ID number is: ", tempIndex)
else:
    print("Employee name is not found. ")

# Q1f
UserInput = input("Please input a letter (P or D) to identify the action for an employee: ")
def Information():
    i = 0
    if UserInput == "P":
        print(AllEmployees[i].GetName(), AllEmployees[i].GetEmployeeID(), AllEmployees[i].GetDepartment())
    elif UserInput == "D":
        