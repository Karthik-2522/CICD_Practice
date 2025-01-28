 
print(a)
a.add('sam')
print(a)
b={5,6,'mon','tue'}
a.update(b)
print(a)
a.remove('mon')
print(a)
a.discard('Tue')
print(a)
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)
c=a.symmetric_difference(b)
print(c)
a.update(c)
print(a)
a={1,2,3,4}
b={5,6,7,8,4}
a.pop()
a.pop()
a.pop()
print(a)
print(a.isdisjoint(b))
print(a.issubset(b))
c=455-260
print(c)

user={"name":"Lakshanya",
        "age":"11 Months",
        "Gender":"Female",
        "weight": "8kg"}
print(user)
print(type(user))
print(user["name"])
print(user.get("name"))
print(user.keys())
print(user.values())
c=user.items()
print(c)
print(type(c))
for i in user:
    if i=='Gender':
        print(True)
    else:
        print(False)
    print(i)
for i in user.keys():
    print(i)
for i in user.values():
    print(i)
for i,j in user.items():
    print(i,j
user.update({'father':'Karthik','mother':'vimala'})
print(user)
user["name"]='Laddu'
print(user)
user.pop("father")
print(user)
users={
    'user1':{"name":"Lakshanya",
        "age":"11 Months",
        "Gender":"Female",
        "weight": "8kg"},
    'user2':{"name":"Karthik",
        "age":"32 Years",
        "Gender":"Male",
        "weight": "67kg"},
    'user3':{"name":"Vimala",
        "age":"29 Years",
        "Gender":"Female",
        "weight": "80kg"}}
print(users)
print(users.keys())
print(users.values())

def lak():
    print("Welcome")
lak()
 no return type without argument
def vim():
    a=int(input("enter value of A:"))
    b=int(input("enter value of b:"))
    c=a+b
    print("Total value :",c)
vim()
 no return type with argument
def kar(a,b):
    c=a-b
    print("Difference :",c)
kar(25,20)


def div():
    a=int(input("enter value of A:"))
    b=int(input("enter value of b:"))
    c=a+b
    return c
d= div()
print(id(d))

def employee(*names):
    for name in names:
        print(name)
employee('lad','vim','kar')

def det(name,age):
    print(name, 'age is', age)
det(age='laddu', name=1)
def data(names):
    print(sum(names))
data(name='laddu',gender='female',age=1)
data([10,15])
def fact(x):
    if x==2:
        print('value1:',x)
        return 2
    else:
        print('value2:',x)
        return (x * fact(x-1))
print('fact',fact(4))

import datetime as dt

current_date=dt.date.today()
print('today date is :',current_date)
a=dt.date(2021,10,31)
print(a)
b=dt.datetime.now()
print(b)
print(b.strftime("%Y_%m_%d_%H_%M_%S"))

import math
print(math.sqrt(9))
print(math.ceil(2.5555))
print(math.floor(3.5555))
print(math.factorial(6))
print(math.fabs(-10))
print(math.pow(5,6))

try:
    a=10/0
except Exception as e:
    print(e)

try:
    a=10/0
except Exception as e:
    print(e)
else:
    print("value of A :",a)
finally:
    print("End of Code")
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

try:
    print(a)
except NameError as e:
    print("A is not Defined")
    
try:
    a=int('Laddu')
except ValueError as e:
    print("Please Enter Numbers Only")
    
try:
    a=[10,20,30,40]
    print(a[5])
except IndexError as e:
    print("Invalid Index")

 try:
     a=open("test1.py")
 except FileNotFoundError as e:
     print("File not found")
 else:
     print(a.read())
 def factorial(x):
     if x>1:
         return x*factorial(x-1)
     else:
         return 1
 a=factorial(7)
 print(a)
 def reverse(value):
     a=""
     for i in value:
         a=i+a
     print(a)
 reverse("Lakshanya")
 def pyramid(n):
     for i in range(n):
         for j in range(n,i,-1):
             print(" ",end="")
         for k in range(i+1):
             print("* ",end="")
         print()
     for l in range(1,n):
         for m in range(l+1):
             print(" ",end="")
         for o in range(n-1,l-1,-1):
             print("* ", end="")
         print()
 pyramid(6) 

 def asc(n):
     for i in range(n):
         for j in range(i+1):
             print("*",end="")
         print()
 asc(5)
 def fib():
     result=[]
     a=0
     b=1
     for i in range(15):
         result.append(a)
         c=a+b
         a=b
         b=c
          print(b)
     print(result)
 fib()
 def fibonacci(n):
     a, b = 0, 1
     result = []
     for _ in range(n):
         result.append(a)
         a, b = b, a + b
     return result
 a= fibonacci(15)
 print(a)

 my_list = [10, 12, 14, 10, 16, 14, 18]

  set to store duplicate elements
 duplicate = set()

 for num in my_list:
      count number of times element appears in the list
     if my_list.count(num) > 1:
         print(num)
         duplicate.add(num)

 print(duplicate)
 a=set(my_list)
 print(a)

b="karthik"
print(b[::-1])
print(b==b[::-1])

from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_anagram("karthi","vimala"))

def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
c=climb_stairs(10)
print(c)