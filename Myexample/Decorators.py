# Decorators are actually used to decorate a function
# They can return a function inside of a function. Also these are the functions which you can also run separately just by using "@" symbol.
# Function inside a function

def func(original_func):            
    def wrap():
        print("Print the code, say, like on the top")
        original_func()
        print("Print the code, say, like on the bottom")
    return wrap()

@func                                     # @ is used in calling func function before original_func to get called
def original_func():
    print("BOX,say, This is the box to be wrapped")


