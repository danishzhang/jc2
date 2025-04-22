# class car: # the same as TYPE car in pseudocode
#     def __init__(self, Make,Model,Color):
#         self.Make = Make
#         self.Model = Model
#         self.Color = Color
#     def start(self):
#         print("The car has started")
#     def stop(self):
#         print("the car stopped)")


# # Instantiation : to make an instance of a class
# # 
# # an object is an instance of a class; car1 is an instance of car(). 
# # From 1 class it can create lots of instances (e.g car2 = car())
# #Constructor : special method written isnide a class used to construct an object
# #allows us to personalise the objects while creation
# # car1.Make = "TOTOYA"
# # car1.Model = "200"
# # car1.Color = "Red"

# car3 = car("Honda","2021","Black")
# car4 = car("BMW","2021","Blue")
# car5 = car("Mercedes","2021","Yellow")

# # 
# # TYPE car:
# #   DECLARE make : STRING
# #   DECLARE model : STRING
# #   DECLARE color : STRING
# # ENDTYPE

# #everytime you try to create instance, python passes the object itself as the argument
# #everytime you write a method inside a class, even it doesnt take 

# print(car3.Model)
# print(car3.Make)
# print(car3.Color)
# car3.start()
# car3.stop()

# print(car4.Model)
# print(car4.Make)
# print(car4.Color)
# car4.start()
# car4.stop()

# print(car5.Model)
# print(car5.Make)
# print(car5.Color)
# car5.start()
# car5.stop()

class Person:
    personCount = 0
    def __init__(self, name, DoB, gender):

        #name, DOB, gender is a variable of an instance (instance variable)
        #non-instance variable is variable that belongs to the class variable
        #and is being defined outside the __init__ 

        #to make these private, add __ in front of the attribute

        self.__name = name # of type string  
        self.__DoB = DoB # of type dat/string
        self.__gender = gender # of type string
        Person.personCount += 1 # Why the output can be 3


    def walk(self):
        print("The person in walking")
    def run(self):
        print("The person is running")

    # Getters and Setters
    #GETTER
    def getName(self): #getters will never take any parameters
        return self.__name

    def getDoB(self):
        return self.__DoB

    def getgender(self):
        return self.__gender

    #SETTER
    def setName(self, name):
        self.name = name 

    def printDetails(self):
        print(f"Name: {self.__name}, Date of Birth: {self.__DoB}, Gender: {self.__gender}")


class Teacher(Person):
    # pass # pass is used to inherit the methods n objects from Person
    #      # Teacher now have everything Person has
    def __init__(self, name, DoB, gender, salary):
        super().__init__(name, DoB, gender) 
        self.salary = salary 
        
    def printDetails(self):
        print(f"Name: {self.getName()}, Date of Birth: {self.getDoB()}, Gender: {self.getgender()}, Salary: {self.salary}")
        # AttributeError is outputted because the name is a private variable that is only specific to Person
        # To overcome this we need to use GETTER

class Student(Person):
    def __init__(self, name, DoB, gender, grade):
        super().__init__(name, DoB, gender)
        self.grade = grade
    def printDetails(self):
        print(f"Name: {self.getName()}, Date of Birth: {self.getDoB()}, Gender: {self.getgender()}, Grade: {self.grade}")
teacher1 = Teacher("Bang Jon", "27/09/1904", "Male", 2000)
student1 = Student("Bang Sudj", "10/01/2007","Male", 90)

# person1 = Person("Ken", "18/02/2007", "Female")
# person2 = Person("Matthew", "01/02/1940", "Male")
# person3 = Person("Seong", "21/01/2007", "Male")

# print(person1.__name, person1.__DoB, person1.__gender)
# print(person2.__name, person2.__DoB, person2.__gender)
# print(person3.__name, person3.__DoB, person3.__gender)
#OR
# print(person1.__dict__) 


# print(person1.personCount)
# # so instead
# print(person1.getName(), person1.getDoB(), person1.getgender())

# person1.printDetails()

teacher1.printDetails()
student1.printDetails()




    
