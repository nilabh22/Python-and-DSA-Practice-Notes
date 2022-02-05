
my_income = 1000 #assigning variables
my_taxes = 20/100
pa = 100/334
x = "Hello Brother"
u= "a","b","c",
n=1,2,3,
total = my_income * my_taxes
print('Rs', total)
print(len(x)) ##################length of string
print("HelloBrother"[-9])
print(x[3:9]) #################Indexing and Slicing
print(x[::2])
print(x[::-1])
print(x[0:5] +'Sister') ####################string concatenation
print(x.upper()) ######to uppercase all letters
print(x.lower()) ###############to lowercase everyletter
print(x.split()) ##############to split the string assigned in gaps
print(x.split('o')) #####################we can actually split tgrough any leter we want
#we can also concatenate the strings in another way using .format
print("Hello Brother{}".format(" Long time no see"))
print("Hello Brother{1} {2} {0}".format("well.", " Long time no see.", "Hope you are doing"))
#Insert the position values in curly braces to rearrange the text in the particular order.
#fill Same no. values in braces to get the same sentence.
print("The principle amount is: {h:1.3f}".format(h=pa)) #float formatting
#LISTS---------------**************-----------------
mylist = ['alter',2,200.19]
print(mylist)
anolist = ['with',12,'help']
newlist = mylist + anolist
print(newlist)
print(newlist[::-1])
newlist.append('hi')
print(newlist)
print(len(newlist))
print(newlist.pop(2))
print(newlist) #"hi" is removed. by default -1 placeholder is removed. I used 2nd placeholder to remove to take it as an example
#DICTIONARY
mydic = {'key1':'apple',"key2": 140,'key3':'apples were good','key4':[100.196845,'oranges',"hEy"]}
print(mydic['key4'][0]) #keep on calling from dictionary no matter its an integer or list.
#advantage of dictionary over a list is that it can be called directly.
print("the round off is: {t:1.3f}".format(t=mydic['key4'][0]))
mydic['key5']= "Hello brother" #adding a new key in the prvious one
print(mydic.keys()) #to see keys
print(mydic.values()) #.....
print(mydic.items()) # directly calls upon items

##############TUPLES#######################
tup= ('a',2,"teabag") #tuples and list has a difference that tuples use parenthesis and list uses square brackets
print(tup)
z = tup.count('a')
f = tup.index('a')
print(f)
print(z) #advantage of tuples over lists is that it cannot be reassigned or changed.
#example : if u forget about some variable you've already given.It will not reassign, else it shows error.
##############SETS#########################
myset = set()
lis=[1,1,1,1,1,2,2,3,3,3,3,4,4,4,4,4]
myset.add(1)
myset.add(2)
print(set(lis)) #to print only unique values out of repeating ones
##############BOOLEANS#####################
print(1==1)
###############I/O operations##############
f = open("lol.txt", "w+") #Operations include modes. r= read only, w= write only, a= append only, r+ =reading and writing, w+ = writing and reading both(also creates new files or overwrites if already existed).
f.write('Hello Human')
f = open("lol.txt","a") #Used "a" to add a new line basically append
f.write("\nyou are a filthy shit.")
f.close()
lol= open('lol.txt')
print(lol.read())

               #######################PYTHON COMPARISON OPERATORS#####################
print('h' == 'h' and 2 == 3)   #"AND" operator returns true if both are true
print(1==1)      #"OR" returns true when even if only one of given is true ....  "NOT" returns the opposite og the boolean thats about to come.

# ######################Python statements############################
name = 'Ajay'
if name == "Ashish":
    print("Vo dekho bsdka")
elif name == "Onkar":
    print("Vo dekho ek or bsdka")
elif name == "Himanshu":
    print("Yes!! He is intelligent")
else:
    print('What is your name?')

#####################For statements#################

for things in mylist:
    print("Hello Humans") #"things" is just a flexible variable name. You can choose anything in place of things which has a relation with the mylist contents.

# Example till

mynum=[1,2,3,4,5,6,7,8,9,10]
for num in mynum:
    if num % 2 == 0:
        print(f"Even number: {num}")     #SomethingNew
    else:
        print(f"Odd number: {num}")      #We can print integer results like this too

listsum = 0
for num in mynum:
    listsum = (listsum + num)
print(listsum)      #If we print listsum inside this for loop then each added value will be printed like 1,3,6,10..... and so on

#Printing Strings through "for" loop

for _ in x:
    print(_)

for items in tup:
    print(items)

laso=[(1,2),(3,4),(5,6),(7,8)]       ##Tuple Unpacking
for (a,b) in laso:
    print(b)

for items in mydic.items():          #Dictionary by default print only key name,so we can either use tuple unpacking or call upon "dic".items() to print both values.
    print(items)

########## WHILE STATEMENTS ###########
a=0
while a<5:
    print(a)
    a+=1
    break

for mynum in range(10):              #Range Function
    print(mynum)

for items in enumerate(x):           #Enumerate fucntion automatically prints (numeral,any thing you've given) and gives tuples as output
    print(items)

for items in zip(n,u):               #ZIP zips down the two lists 
    print(items)

# IMPORTING LIBRARIES

from random import randint               #To choose random integers
print(randint(3,288))

###################### INPUT FUNCTION IS IN VSCode ################

######## List Comprehension -: It appends in the list.

mylist0 = [s for s in "word"]
print(mylist0)

mylist2 = [f for f in range (1,11) if f%2 == 0]    #We can also use "if" statements in between the braces after the "for" statements
print(mylist2)

#Question - Convert a list of celcius temperatures in farenhiet. Celcius = [0, 10, 23, 38.6, 42.5]

celcius = [0, 10, 23, 38.6, 42.5]

farenhiet = [((9/5)*temp +32) for temp in celcius]      #List comprehension
print(farenhiet)
#  Another way of doing same is----

farenhiet = []
for temp in celcius:                                   #Old method but better readability
    farenhiet.append((9/5)*temp + 32)
print(farenhiet)

results  = [x if x%2== 0 else 'Odd' for x in range(1,11)]     # To use if and else list comprehension
print(results)

mylist1 = []
for x in [2,4,6]:
    for y in [1,10,1000]:             # Nested Loop
     mylist1.append(x*y)

# Same by list comprehension

mylist1 = [(x*y) for x in [2,4,6] for y in [1,10,1000]]     # Less readability
print(mylist1)


# Write a program to print integers from 1 to 100 but print fizz for multiples of 3 and buzz for multiples of 5.

for g in range(0,101):
    if g%3 == 0 and g%5 == 0:
        print("FIZZBUZZ")
    elif g%3 ==0:
        print("FIZZ")
    elif g%5==0:
        print("BUZZ")
    else:
        print(g)

# Practice examples
st = 'Create a list of the first letters of every word whose length is even in this string' #using list comprehension.
jo =[po[0] for po in st.split() if len(po) %2==0 ]
print(jo)

#  METHODS AND FUNCTIONS

def say_name(name):
    print(f"Hello {name}")    #To assign a function we use "def"
say_name('Nilabh')

def add(num1, num2):
    print(num1+num2)
add(5,7)

def even_num(num):
    return num%2==0        ## By using return we can actually assign the function later
c=even_num(8)
print(c)

def even_num_list(num_list):
    for number in num_list:
        if number %2==0:
            return True
        else:
            pass

#Write a program to print the even number in a list if they are prsent in a list given by a user

even_numbers =[]
def even_num_lists(num_list):
    for number in num_list:
        if number %2==0:
            even_numbers.append(number)
        else:
            pass

print(even_num_list([1,2,4,6,5,9]))
print(even_num_lists([1,2,4,6,5,9,11,12,14]))

# Program that prints employee of the month along with employee name and his working hours on the basis of working hours.

name_hours = [("Mihir",100),("Onkar",801),("Nilabh",926),("Ajay",800)]
def employee_month_check(name_hours):

    max_hours = 0
    employee_of_the_month = ""

    for employee,hour in name_hours:
        if hour > max_hours:
            max_hours = hour
            employee_of_the_month = employee
        else:
            pass

    return (employee_of_the_month,max_hours)

v=employee_month_check(name_hours)
print(v)

# Guessing Game

from random import shuffle                # shuffing a random list

game = [' ','O',' ',' ',' ',' ',' ',' ']
def shuffle_list(game):
    shuffle(game)
    return game
ui=shuffle_list(game)
print(ui)

# *Args amd **kwargs


def myfunc(*args):
    return sum(args)     # *args if given in a defined function, we can find sum of numbers upto many no. of places(sum for 10,10,10,10,10,.....n times without giving position holders inthe defined function
gg=myfunc(20,10,100)
print(gg)

def func(**kwargs):        # kwargs returns the input in the form of a dictionary
    print(kwargs)
func(fruit ="apple", veggie="spinach")

# We can also use the args and kwargs simultaneously in the function and the input must be in the order of arguements give

# Example 1- Given two integers, return true if the sum of the integers is 20 or even if one integer is 20. If not, return false.

def sum_twenty(n1,n2):
    print(n1 ==20 or n2== 20 or n1+n2 ==20)
sum_twenty(10,5)

# Example 2- Write a program that capitallize the first and 4th letter of the name.

def old_macdonald(name):
    first_part = name[:3]
    second_part = name[3:]
    return first_part.capitalize() + second_part.capitalize()

oo=old_macdonald("macdonald")
print(oo)

# Example - WAP that reverses the given string

def reverse(text):
    mytext = text.split()
    reverse_list =mytext[::-1]
    return " ".join(reverse_list)
kk=reverse("I am ready")
print(kk)

# Example - Given an integer n, return true if n is within 10 of either 100 or 200
# abs concept
def almost_there(n):
    return abs(100-n)<=10 or abs(200-n)<=10
uii=almost_there(111)
print(uii)

# Given a string, return a string where for every character in original there are 3 characters.
# Text ----> "Mississippi"
def three_letter(text):
    result = ""
    for char in text:
        result = result+ char*3
    return result

mk=three_letter('Hello')
print(mk)

# Write a function that takes in a list of integers and returns true if it contains 0,0,7 in order
# spy_game([1,2,4,0,0,7,5]) -----> True
# spy_game([1,7,2,0,4,5,0]) -----> False
def spy_game(nums):
    codelist = [0,0,7,'x']
    for num in nums:
        if num== codelist[0]:
            codelist.pop(0)
    return len(codelist)==1

ll=spy_game([1,7,2,0,4,5,0])
print(ll)

# Lambda, Map and Filter function

# Map function takes a function and iterate through the input map(func,input)


def square(nums):
    return nums**2

nums =[1,2,3,4,5]
for item in map(square,nums):                  #map function
    print(item)

mi=list(map(lambda nums:nums*10,nums))            # Lambda function simplifies the def part and return in to same one line
print(mi)

# Palindrome

def palindrom(s):
    s= s.replace(' ','')
    s= s.lower()
    return s== s[::-1]                  # Palindrom
print(palindrom("nU rse s run"))

# Pangram - all alphabets should be present at least 1 time

alphabet = "The Quick Brown Fox Jumps Over the Lazy Dog"
import string
def pangram(strg1, alphabet= string.ascii_lowercase):
    alphaset = set(alphabet.lower())
    strg1 =strg1.replace(' ','')
    strg1 = strg1.lower()
    strg1= set(strg1)
    return alphabet== alphaset

print(pangram("The Quick Brown Fox Jumps Over a Lazy Dog"))


