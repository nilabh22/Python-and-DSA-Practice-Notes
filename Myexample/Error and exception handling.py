# There are basically three mains terms that are used n error and exception handling

# 1. try: - We will write our code that we wanted to execute Under this "try()" menthod.
# 2. except: - This is used when there is an error and it will print whatever you command to print.
# 3. else: - It will run when there is no error in code under try() method.
# 4. finally: - This will run no matter what.

try:
    f= open("Noob.txt","w")
    f.write("The Noobs have a K/D ratio of less than 2.0")        # The code will run
    f.close()
except:
    print("Oh! There is a error")                  # Since there is no error ir printed
else:
    print("Ah shit! There is no error")         # No error
finally:
    read= open("Noob.txt")                     # No matter error or what
    print(read.read())

def Ask_for_int():
    while True:
        try:
            result = int(input("Enter a Number: "))
        except:
            print("That is not a number!")
        else:
            print("Thank You")
            break

Ask_for_int()
