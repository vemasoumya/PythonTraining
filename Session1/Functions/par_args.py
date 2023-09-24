""" parameters 
non default 
default 
arbitrary 
"""

def func1(a = 1, b=2):
    return a + b

def func2 (a , b = 2):
    return a + b

#non default cannot follow default
# def func3 ( a = 1, b):
#     return a + b

def func3(*args):
    print(type(args))
    return args 

def func4(**kwargs):
    print(type(kwargs))
    return kwargs 

#positional arguments
print(func1())
print(func2(10))
print(func2(10,5))
print(func3())
print(func3(1,2))
print(func4())
print(func4(a=1, b=2))

#keyword arguments
print(func2(a = 1))




