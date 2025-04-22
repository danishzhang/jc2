# class Library:
#     def __init__(self, name):
#         self.__name = name
#         self.__books = []

#     def addbook(self, book):
#         self.__books.append(book)
    
#     def printLibraryBooks(self):
#         for book in self.__books:
#             print(book.getName(), book.getAuthor(), book.getDate())

# class Book:
#     def __init__(self, title, author, publish_date):
#         Book.__title = title
#         Book.__author = author
#         Book.__publish_date = publish_date
#     def getName(self):
#         return self.__title
#     def getAuthor(self):
#         return self.__author
#     def getDate(self):
#         return self.__publish_date


# bbs_library = Library("Bina Bangsa School Library")
# book1 = Book("The Mogger", "Ken", "11/9/2023")
# book2 = Book("Harry Potter", "Karel", "21/01/2009")

# bbs_library.addbook(book1)
# bbs_library.addbook(book2)
# bbs_library.printLibraryBooks()


import pickle
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alex", 16)
student2 = Student("ken", 20)
file = open("Student.dat", 'wb') 
# wb stands for write binary
pickle.dump(student1,file)
pickle.dump(student2,file)
# the information of studetnt 1 is dumped into the file
file.close()

file = open("Student.dat", 'rb')
tempStudent1 = pickle.load(file)
tempStudent2 = pickle.load(file)
file.close()

print(tempStudent1.name)
print(tempStudent1.age)

print(tempStudent2.name)
print(tempStudent2.age)