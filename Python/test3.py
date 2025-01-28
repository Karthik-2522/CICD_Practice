class student:
    count=0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.count+=1
    def printall(self):
        print("Name :",self.name, "Age",self.age)
    @classmethod    
    def total(cls):
        return cls.count
a=student("laddu",1)
a.printall()
a=student("vimala",29)
a.printall()
print(a.total())

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printall(self):
        print("Name : ",self.name," Age : ",self.age)
    @classmethod
    def welcome(cls):
        print("Welcome to the World")
a=student('Karthik',32)
student.printall(a)
student.welcome()

class library:
    def __init__(self,books):
        self.books=books
    def list_books(self):
        print("available Books are : ")
        for book in self.books:
            print(book)
    def borrow_books(self,book):
        print("you've borrowed the Book : ",book)
        self.books.remove(book)
    def return_books(self,book):
        print("you've Returned the Book : ",book)
        self.books.append(book)

book = ['java','python','c++']
a=library(book)
msg = 
Please select the Option
1. View Available Books
2. Borrow Books
3. Return Books
while True:
    print(msg)
    ch = int(input("Please Enter your Choice : "))
    if ch==1:
        a.list_books()
    elif ch==2:
        book_name=input("Please Enter Book Name to Borrow: ")
        a.borrow_books(book_name)
        print("PLease Get your Book")
    elif ch==3:
        book_name=input("Please Enter Book Name to Return: ")
        a.return_books(book_name)
        print("You are Welcome")
    else:
        print("Thank you Come Again")
        quit()  

a.list_books()
a.borrow_books('java')
a.list_books()
a.return_books('java')
a.list_books()
a.return_books('java')
a.list_books()

    