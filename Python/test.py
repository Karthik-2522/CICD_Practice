"""a=25
b=30
c=b-a
print(c)
print(a+b)
print(b)"""

"""a=input("Enter your name :")
print("your name :" +a)
print(type(a))
c=int(input("value1 :" ))
d=int(input("value2 :" ))
print(c+d)"""

"""name1, name2,name3=input("enter 3 names :" ).split()
print("name1 :" ,name1)
print(name2)
print(name3)"""

''' para = ["A","B","C"]
 print(''.join(para))

para=[]
print("Enter a para :")
while True:
	line=input()
	if line:
		para.append(line)
	else:
		break
print(para)
print('\n'.join(para))
a="Python learning exercise"
print(type(a))
print(type(int(a)))
print(a)
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.count('o'))
print(a.endswith('ng'))
print(a.find('a'))
print(a.find('a',3))
print(a.replace('a','i'))
print("is uppercasr",a.isupper())
print("is lower", a.islower())
print("is alphanumeric",a.isalnum())
print("splitted",a.split( ))
print(len(a))
print(len(a.strip()))
string Maniplulation
string slicing
a='sample'
print(a)
print(a[0:3])
print(a[2:1])
print(a[-2:-3])
print(a[::-2])
arithmetic operation
a= 10
b= 25
c= 10
if a<=b and a>=c:
    print("true")
else:
    print("false")
    
a=int(input('enter a number :'))
if a%2 == 0:
    print("Entered no",a,"is Even")
else:
    print("Entered no",a,"is odd")
days=int(input('Enter No of days :'))
if (days==0):
    Print('you are Good No fine')
elif (days>=1 and days<=5):
    print('you are',days,'late and your fine will be :',days*0.5)
elif (days>5 and days<=10):
    print('you are',days,'late and your fine will be :',days*1)
elif (days>10 and days<=30):
    print('you are',days,'late and your fine will be :',days*5)
else:
    print('you are',days,'late and your membershib canceled')

m1=int(input('Enter mark1 :'))
m2=int(input('Enter mark2 :'))
m3=int(input('Enter mark3 :'))
total = m1+m2+m3
print(int(total))
average = total/3
print(int(average))
if(m1>35 and m2>35 and m3>35):
    print('you are pass')
    if(average>=70 and average<=79):
        print('your grade is C')
    elif(average>=80 and average<89):
        print('your grade is B')
    elif(average>=90 and average<=100):
        print('your grade is A')
    else:
        print('your grade is D')
else:
    print('you are fail')
 
i=1
while i<=10:
    if i%2==0:
        i=i+1
        print('a',i)
        continue;
    print('b',i)
    i+=1
for i in range(6):
     print(i)
    for j in range(i):
        print("*", end="")
    print('')
for i in range(5):
    for j in range(5,i,-1):
        print(" ", end="")
    for k in range(i+1):
        print("* ",end="")
    print()
for l in range(1,5):
    for m in range(l+1):
        print(" ",end="")
    for n in range(5-1,l-1,-1):
        print("* ", end="")
    print()
    
 for i in range(5,0,-1):
     for j in range(i):
         print("*", end="")
    
    
     print("")

a = [0,1,2,'laddu','vimala',True,1.0]
print(a[0])
print(a[0:2])
print(a[-1])
print(a[-5:-1])
print(a[-3:-1])
print(a[0],'type is',type(a[0]))
print(a[1],'type is',type(a[1]))
print(a[2],'type is',type(a[2]))
print(a[3],'type is',type(a[3]))
print(a[4],'type is',type(a[4]))
print(a[5],'type is',type(a[5]))
print(a[6],'type is',type(a[6]))
b=[0,1,2,3,4,25]
print(b)
b[2]=25
print(b)
print(len(b))
print(b.count(25))
print(b.index(25, 3))
print(max(b))
print(min(b))
a=[1,2,3,4]
b=['ram','sam','mom','dad']
a.extend(b)
print(a[0],':',a[4],a[1],':',a[5],a[2],':',a[6],a[3],':',a[7])
print(list(range(6)))
print(list("vimala"))
a=[0,1,5,2,5,8,7,9]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=['a','at','Karthi','vimala','laddu']
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(chr(70))
a=(0,1,2,3,'laddu')
print(a)
print(type(a))
b=list(a)
print(type(b))
b.append('Vimala')
a=tuple(b)
print(type(a))
print(a)
i=[10]
for j in range(10) :
    print(j)
for j in i:
    if 10 in i:
        print("Found")
    else:
        print("not found")
b=(1)
c=(2)
d=(3)
print(b,c,d)

a=[1,2,3]
a.insert(4,'ram')
print(a)
 Python program to illustrate the intersection
 of two lists in most simple way
 def intersection(lst1, lst2):
     lst3 = [value for value in lst1 if value in lst2]
     return lst3

  Driver Code
 lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
 lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
 print(intersection(lst1, lst2))
 def intersect(list1,list2):
     set(list1)
     set(list2)
     c=[set(list1) & set(list2)]
     return list(set(list1) & set(list2))
 c=intersect(lst1,lst2)
 print(c)
a="karthik"
b="vimala"
print(list(a))
print(set(a))
print(dict(b,a))'''

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
m = fibonacci_iterative(0)
print(m)


