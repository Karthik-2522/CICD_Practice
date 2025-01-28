class car():
    pass
a=10
print(type(car))
swift=car()

print(isinstance(a,int))
print(isinstance(swift,car))
print(type(swift))

class student():
    a='name'
    b=10
laddu=student()
print(getattr(student,'a'))
print(getattr(student,'default','no such attribute'))
print(laddu.a)
setattr(student,'a','vimala')
setattr(student,'c','karthik')
print(laddu.a)
print(laddu.c)
print(laddu.__dict__)
print(student.__dict__)
del student.c
print(laddu.__dict__)

class user:
    name='laddu'
    age=1
    gender='female'
    
    def printall(self):
        print("Name :", user.name)
        print("Age :", user.age)
        print("Gender :", user.gender)
a=user()
print(user.__dict__)
user.printall(a)
print(getattr(user,'printall'))
getattr(user,'printall')(a)
user.__dict__['printall'](a)
a.printall()

class user:
    def __init__(self, name,age,gender):
        print("new instance creation")
        self.name=name
        self.age=age
        self.gender=gender
        self.msg=self.name+ " is " + str(self.age) +" year old " + self.gender
    @property
    def msg(self):
        return self.name+ " is " + str(self.age) +" year old " + self.gender
        
a=user('laddu',1,'female')
print(a.msg)
a.age=2
print(a.age)
print(a.msg)

class student:
    def __init__(self, total):
        self.total=total
    @property
    def average(self):
        return self.total/5.0
a=student(480)
print("total value :",a.total)
print("total average :",a.average)

class student:
    def __init__(self,total):
        self._total=total

    def average(self):
        return self._total/5.0
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self,t):
        self._total=t
    
a=student(450)
print(a.total)
print(a.average())
a.total=300
print(a.total)
print(a.average())

class student:
    def __init__(self,total):
        self._total=total

    def average(self):
        return self._total/5.0
    
    
    def getter(self):
        return self._total
    
 
    def setter(self,t):
        self._total=t
    total=property(getter,setter)
    
a=student(450)
print(a.total)
print(a.average())
a.total=300
print(a.total)
print(a.average())



        



