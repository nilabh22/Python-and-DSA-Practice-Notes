# Generators basically use "yield" function instead of "return" when you create a "def" function
def cube_num(n):
    cubes= []
    for x in range(n):
        cubes.append(x**3)
    return cubes

print(cube_num(11))

def cube_num(n):
    for x in range(n):
        yield x**3

print(list(cube_num(11)))

# Creation of fibonacci series

def fibonacci(n):
    a=0
    b=1
    for x in range(n):
        yield a               # Using Generator (Yield is used to return this)
        a,b = b,a+b
print(list(fibonacci(11)))

def fab(n):
    a=0
    b=1
    fabo =[]
    for i in range(n):       # Old method
        fabo.append(a)
        a,b = b,a+b
    return fabo
print(fab(11))