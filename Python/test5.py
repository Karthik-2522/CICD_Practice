 $ python -m pdb test4.py
def testgen(index):
    weekdays = ['sun','mon','tue','wed','thu','fri','sat']
    yield weekdays[index]
    yield weekdays[index+1]
day = testgen(0)
print (next(day), next(day))

a=[1,2,3]
s=['hello','world']
b=str(a)
c=tuple(a)
d=' '.join(s)
print(type(a))
print(type(b))
print(type(c))
print('a',a)
print('b',b)
print('c',c)
print('d',d)

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print([[x,weekdays.count(x)] for x in set(weekdays)])
for x in set(weekdays):
    print(x,weekdays.count(x))
    
a=[1,2,3]
print(a[-2 -1])
for i, a in enumerate(a):
    print(i,a)
sum=0    
for i in range(1,101):
    sum+=i
print(sum)
print("sum", sum(range(1,101)))