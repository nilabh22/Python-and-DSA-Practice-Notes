class Talent():

    college = "Central University of Haryana"
    def __init__(self,singer,artist,writer):
        self.singer = singer
        self.artist = artist
        self.writer = writer

    def presentation(self):
        print(f"My name is {self.singer}")
        print(f"My name is {self.artist}")
        print(f"My name is {self.writer}")

my_talent = Talent(singer="Sarthak", artist="Nilabh", writer="Kush")

print(my_talent.college)
print(my_talent.writer)
print(my_talent.artist)
print(my_talent.singer)
my_talent.presentation()

# Inheritance and Polymorphism
# Inheritance is basically inheriting the instances from a base class.

class Animal():
    def __init__(self):
        print("Animals Created")

    def what_r_u(self):
        print("I am a animal")

    def eat(self):
        print("I can eat")

my_animal = Animal()
my_animal.eat()
my_animal.what_r_u()

class Cat(Animal): # Animal is base class and is inherited to "Cat" class
    def __init__(self):
        Animal.__init__(self)
        print("Cat Family")
    def what_r_u(self):
        print("I am a CAT")

mycat = Cat()
mycat.eat() # Here, .eat is been inherited from Animal class
mycat.what_r_u()

##############  POLYMORPHISM ################
class Dog():
    def __init__(self,name):
        self.name= name
    def speak(self):
        return self.name + " says Woof!"

class Cat():
    def __init__(self,name):
        self.name= name
    def speak(self):
        return self.name + " says meow!"

niko = Dog("Niko")
felix = Cat("Felix")

for pet in [niko,felix]:
    print(pet.speak())          # Polymorphised speak() function by iterating through both classes using for loop

############### MAGIC LITERALS ###################

class Book():
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"The Book {self.name} is by {self.author}"
    def __len__(self):
        return self.pages

my_book= Book('Harry Potter','J.K Rowling',520)
print(my_book)
print(len(my_book))

################ HomeWork Assignment ###############
######### WAP that returns the distance and slope between two coordinates #########

class Line():
    def __init__(self,coor1,coor2):
        self.coor1= coor1
        self.coor2= coor2

    def Distance(self):
        x1,y1 =self.coor1
        x2,y2 =self.coor2

        print(((x2-x1)**2 + (y2-y1)**2)**0.5)

    def Slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        print(y2-y1/x2-x1)

c1=(2,5)
c2=(8,11)
line= Line(c1,c2)
line.Distance()
line.Slope()

####### WAP that returns the volume and surface area of a cylinder given default radius=1 and height =1 ##########
class Cylinder():
    def __init__(self,height=1,radius=1):
        self.height= height
        self.radius= radius
    def Volume(self):
        print(3.14*self.radius*self.radius*self.height)
    def Surface_area(self):
        top = 3.14 * self.radius**2
        print(2*top + (2* 3.14* self.radius * self.height))

cylinder = Cylinder(15,7)
cylinder.Volume()
cylinder.Surface_area()

#########  CHALLENGE QUESTION from OOP  ##############

class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def Deposit(self,amount):
        self.balance = self.balance + amount
        print(f"New Updated Balance: {self.balance}")

    def Withdraw(self,amount):
        self.balance = self.balance - amount
        if amount < self.balance:
            print(f"New Updated Balance: {self.balance}")
        else:
            print("Bhikhaari Itne paise to daal le account me")


acct1 = Account('Nilabh',1000)
print(f"Account Owner: {acct1.owner}")
print(f"Account Balance: {acct1.balance}")
acct1.Deposit(125)
acct1.Withdraw(200)







