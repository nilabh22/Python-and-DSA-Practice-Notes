# 1 - Importing Counter from collections
# Counter - It basicaly returns the count of anything (integer or string) that is passed into it

from collections import Counter
mylist = [1,1,1,1,3,3,3,4,5,4.4,4,5,5,5,5,6,6,6,6]
mylist2 = ['iamabigboy']
print(Counter(mylist))
print(Counter(mylist2))
print(Counter('aaaaaaaajnjdknahgasionflksd'))

c = Counter('I am a big boy and boy are a great species'.lower().split())
print(c)

# 2 - Importing defaultdict from collections
# It will assign a default value to a key that ypu searched thta is not present in the dictionary at that time

from collections import defaultdict
d= {'a':100} # we assigned a dictionary
print(d)
d['f'] = 200  # we iterate for key that is not present previously but we assigned it with a vavlue = 200
print(d)
d= defaultdict(lambda : 0) # lambda :0 will assign every default value of key to 0
d['wrong key!!'] # This key doesnt exist in the dictionary we created but it doesn't shows any key error
print(d)

# 3 - importing namedtuple from collections
from collections import namedtuple
Dog = namedtuple('Dog',['breed','age','name'])
Doggy = Dog(breed='Husky',age=4,name='Sammy')      # Its like creating a class
print(Doggy)
print(Doggy.name)

# 4 - importing os
import os
print(os.getcwd())    # getcwd() will show the current working directory

f= open('newtxt.txt','w+')
f.write("This is a new text")
f.close()

print(os.listdir('C:\\Users'))     # listdir() will show the list of everything that's in the directory you've been on!!

# 5 - importing ShutUtility command
import shutil
#shutil.move('newtxt.txt','C:\\Users\\Nilabh Sahu\\PycharmProjects')    # It moves the source to the destination

# 6 - Importing DateTime Modules

import datetime
print(datetime.date(2021,9,22))
print(datetime.time(14,45,54,104))
print(datetime.datetime(2021,9,22,14,45,54,104))

from datetime import date
date1= date(2021,9,22)
date2= date(2020,9,22)

results = date1-date2
print(results)
print(results.days)

from datetime import datetime
datetime1 = datetime(2021,9,22,22,40,55,101)
datetime2 = datetime(2020,9,22,12,30,44,103)
res = datetime1 - datetime2
print(res.seconds)
print(res.total_seconds())

# 7 - Importing math modules

import math
print(math.pi) # It returns the value of pi
print(math.floor(3.35)) # It returns the integer part of a decimal number
print(math.ceil(3.35)) # It returns the +1 of the interger part of the decimal number
print(math.e)
print(math.log(math.e,2)) # math.log(x, base=)
print(math.sin(90)) # It will return the result in radians
print(math.degrees(math.pi/2)) # To covert radians into degrees
print(math.radians(180)) # to covert radians into degrees

# 8- Importing random modules

import random
print(random.randint(0,100)) # Randint (RandomInteger) returns a random interger from selected numbers
def seed():
    random.seed(42) # Seed basically plants a seed with any arbitraty number and randint will return random intergers but same everytime
    print(random.randint(0, 100))
    print(random.randint(0, 100))
    print(random.randint(0, 100))
    print(random.randint(0, 100))
seed()

import random
las=[]
for i in range(0,21):
    las.append(i)
    if len(las) > 20:
        print(las)
    else:
        continue
print(random.choice(las))

# 9 - Python Debugger

import pdb
x = [1,2,3]
y=2
z=3
result1= y+z
# pdb.set_trace() - # It leaves a trace , since we know result2 is going to give an error, we can go through values.
# result2=x+z
print(result1)

# 10 - Python Regular expressions
# We can find anything in a text like ("phone" in "The phone is expensive") and it will return true.
# But if we do want to find something that is in a perticular format like phone no., email
# We know phone number's format is (XXX)-XXX-XXXX or an email's format is user@email.com
# Then we use "re" module

import re
text = "The world is going to end tomorrow so call on world helpline 111-234-7777 or email us at care@hotmail.com"
print(re.search('world',text)) # It searches world only 1 time
print(re.findall('world',text)) # It searches "world" in whole text
# To combine these two in on we have to itarate through the text
for every_match in re.finditer('world',text):
    print(every_match.span()) # span() - if we want the exact location of that string term
    print(every_match.group()) # group() - if we want to get the text
print(re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)) # we used \d as digit search
print(re.search('\d{3}-\d{3}-\d{4}',text)) # Same thing but we used "QUANTIFIERS"
print(re.search('\S+@\S+',text))
# Additonal Regex Syntax
# Wildcard syntax, period
print(re.search(r'cat | dog','The dog is sitting there')) # '|' is pipe operator and acts as 'OR' operator
print(re.findall(r'.at','The cat in the hat went splat')) # '.' is period operator that print the actual word attached to 'at'.
# ADD more '.' to select more words attached to 'at'.
print(re.search('^\d','1 is a number')) # '^' means starts with, so '^\d' means the string we are searching starts with a digit.
print(re.search('\d$','The one i spell of 1')) # '$' means ends with
# r'[^\d]+' - To remove something from a sentence (\d - digits)


# 11 - Timeit Module
# It calculate time took to run a particular piece of code
def func_one(n):
    return [str(num) for num in range(n)]
def func_two(n):
    return list(map(str,range(n)))
import time
# Calculate time before
time1 = time.time()
# Run Code
result = func_one(1000000)
# Time After running code
time2 = time.time()
elapsed_time = time2-time1
print(elapsed_time)

# Calculate time before
time1 = time.time()
# Run Code
result = func_two(1000000)
# Time After running code
time2 = time.time()
elapsed_time = time2-time1
print(elapsed_time)

# As we can see, mapping is bit faster than list comprehension, but time module is limited. It cannot give precise value to very small code.
# For that we have "timeit" module
import timeit
stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt,setup,number=10000))

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt2,setup2,number=10000))
# As we can see in the results that "timeit" module is much better and faster and precise than the "time" module.

# 12 - Zipping and unzipping modules
# Simply compress files into one folder and we can also extract them.

f= open('file_one.txt','w+')    # FILE_1
f.write('This is file number one')
f.close()

f= open('file_two.txt','w+')    # FILE_2
f.write('This is file number two')
f.close()

import zipfile
comp_file = zipfile.ZipFile('comp_file.zip','w')     #  Create a folder in which all file are gonna compressed
comp_file.write('file_one.txt',compress_type= zipfile.ZIP_DEFLATED)         # We use write for file 1
comp_file.write('file_two.txt',compress_type= zipfile.ZIP_DEFLATED)         # We use write for file 2
comp_file.close()
# We have to extract the files
extracted_files = zipfile.ZipFile('comp_file.zip','r')
extracted_files.extractall('Extracted_files')

# SInce in line 203, 204, we have to add files separately
# SHELL UTILITY method will be help to archieve an entire folder
import os
print(os.getcwd()) # Shows current working directory

import shutil
path = 'C:\\Users\\Nilabh Sahu\\PycharmProjects\\Myexample\\Extracted_files'
output_filename = 'archieved folder'
shutil.make_archive(output_filename,'zip',path)  # This is to turn a folder into an archive
# TO TURN ZIPPED FILE INTO FOLDER THROUGH SHUTIL
shutil.unpack_archive('archieved folder.zip','C:\\Users\\Nilabh Sahu\\PycharmProjects\\Myexample\\archieved folder','zip')

# Reading a file here

with open('C:\\Users\\Nilabh Sahu\\PycharmProjects\\newtxt.txt') as f:
    content = f.read()
    print(content)
