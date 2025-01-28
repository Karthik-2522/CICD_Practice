import pickle

class lakshanya():
    def __init__(self,name,age):
        self.age=age
        self.name=name

    def display(self):
       print(self.name,"is age of", self.age) 
f= open("abc.pdf","wb")
lak=lakshanya("lakshanya", 1)
pickle.dump(lak,f)
print("pickled information is successful")
f=open("abc.pdf","rb")
lakobj=pickle.load(f)
print("unpickling successful")
lakobj.display()
