#Single inheritance
'''class Rntbci:
    company="RNTBCI"
    website="rntbci.com"
    def contact_details(self):
        print("Mahindra City Chengalpattu")
class employee(Rntbci):
    def __init__(self):
        self.name = "Karthik"
        self.zid="Z033238"
    def employee_details(self):
        print("Emp Name : ",self.name)
        print("Emp ZID : ",self.zid)
        print("Company Name : ",self.company)
        print("Company website : ",self.website)
a=employee()
a.employee_details()
a.contact_details()'''

#multiple inheritance
'''class dad:
    name="Karthik"
    age=32
    def dad_hobby(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("playing games")
    def location(self):
        print("Kalambur")
class mom:
    name="vimala"
    age=29
    def mom_hobby(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("watching videos")
    def location(self):
        print("Avadi")
class daughter(mom,dad):
    name="laddu"
    age=1
    def laddu_hobby(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("playing with toys")
    #def location(self):
     #   print("Kelambakkam")
a=daughter()
a.location()'''

'''class GrandFather:
    def ownHouse(self):
        return print("Granpa House")
class Father(GrandFather):
    def ownBike(self):
        return print("Father's Bike")
class Son(Father):
    def ownBook(self):
        return print("Son has Book")
a=Son()
a.ownHouse()
a.ownBike()
a.ownBook()'''

'''class Employee:
    def workinghrs(self):
        self.hrs=50
    def printhrs(self):
        print("working Hours is : ",self.hrs)
class Trainee(Employee):
    def workinghrs(self):
        self.hrs=60
    def resethrs(self):
        super().workinghrs()
a=Employee()
a.workinghrs()
a.printhrs()

b=Trainee()
b.workinghrs()
b.printhrs()

b.resethrs()
b.printhrs()
class a:
    def display(self):
        print("A")
class b(a):
    def display(self):
        print("B")
class c(a):
    def display(self):
        print("C")
class d(b,c):
    def display(self):
        print("D")
z=d()
z.display()'''

'''class addition:
    def __init__(self,a):
        self.a =a
    def __add__(o1,o2):
        return o1.a+o2.a
    def __sub__(o1,o2):
        return o1.a-o2.a
o1=addition(20)
o2=addition(14)
print("total",o1.a+o2.a)
print("Sub value : ",o1.a-o2.a)'''
#abstract method
'''from abc import ABC, abstractmethod
class master(ABC):
    @abstractmethod
    def A(self):
        pass
    @abstractmethod
    def B(self):
        pass
    @abstractmethod
    def C(self):
        pass
class student(master):
    def A(self):
        print("Value A")
    def B(self):
        print("Value B")
    def C(self):
        print("Value C")
s=student()
s.A()
s.B()
s.C()'''

'''try:
    file=open("Text.txt","r")
    print(file.read())
    #file.write("Python")
    #print(file.read())
except FileNotFoundError as e:
    print("Error : File not found")
else:
    file.close()'''
    
'''try:
    file=open("Text.txt","r")
    print(file.readline())
    print(file.readline())
    print(file.readline(5))
except FileNotFoundError as e:
    print("Error : File not found")
else:
    file.close()'''
'''try:
    file=open("Text.txt","w")
    file.write("python")
    file.close()
    file=open("Text.txt")
    for line in file:
        print(line)
except FileNotFoundError as e:
    print("Error : File not found")
else:
    file.close()'''    
    
'''try:
    file=open("Text.txt","a")
    file.write("\njava")
    file.close()
    file=open("Text.txt",'r')
    for line in file:
        print(line)
except FileNotFoundError as e:
    print("Error : File not found")
else:
    file.close() '''
'''import os
if os.path.exists("Text1.txt")  :
    os.remove("Text1.txt")
else:
    print("File not found")
a=[1,2]
for i in range(3,100+1):
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            a.append(i)
             
print(a)
print("total prime in between 1 to 100 is : ",len(a))'''

'''def chk(num):
    if num%2==0:
        print("given no" ,num,"is Even")
    else:
        print("given no" ,num,"is odd")
chk(8)
chk(5)'''
'''def max_no():
    a = int(input("first no :"))
    b = int(input("second no :"))
    maximum = max(int(a),int(b))
    print(maximum)
max_no()'''

'''import math

def factorial(num):
    return (math.factorial(num))

print(factorial(9))'''

'''def sqrt(num):
    s=num**0.50
    print(s)  
sqrt(4)
sqrt(5)'''

'''num=int(input("Enter the number to check armstrong number: "))

#Assigning the num value to arms
arms = num

#Finding the length of the number
length = len(str(num))
sum1 = 0

#Iterating the values to check armstrong number
while num != 0:
	rem = num % 10
	sum1 = sum1+(rem**length)
	num = num//10
print(rem)
print(sum1)
print(num)
#Printing the result whether the given number is armstrong number or not
if arms == sum1:
	print("The given number", arms, "is armstrong number")
else:
	print("The given number", arms, "is not an armstrong number")'''
    
a=[1,2,3,4,5]
b=sum(a)
print(b)


driver = webdriver.chrome()
driver.get()
print(driver.title)
username = driver.find_element(By.NAME,'karthik')
username.click()
input = driver.find_element(By.ID,'vimala')
input.send_keys('laddu')
a=driver.find_element(By.CLASS_NAME,'mohan')
print(a.text)
driver.quit()

driver=webdriver.chrome()
driver.get()
alert=driver.find_element(By.ID,'soffi')
alert.click()
ah=driver.switch_to_alert
print(ah.text)
ah.accept()
driver.quit()

driver=webcriver.chrome()
driver.get()
a=driver.find_element(By.XPATH,'archana').click()
driver.switch_to.frame("frame_id")
driver.save_screenshot()
wait=WebDriverWait(driver,10)
element=wait.until(a.element_to_be_clickable(By.ID,'ID')).click()

driver = webdriver.chrome()
driver.get()
print(driver.title)
driver.execute_script('alert("Hello")')
