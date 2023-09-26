""" parameters 
non default 
default 
arbitrary 
"""
print("default parameters")
def func1(a = 1, b=2):
    return a + b
print(func1())
print(func1(3,3))

def func2 (a , b = 2):
    return a + b
print("*******positional arguments***********") 
print(func2(10))
print(func2(10,5))
print("keyword arguments")
print(func2(a = 1))

#non default cannot follow default
# def func3 ( a = 1, b):
#     return a + b

print("*******arbitrary parameters********")
def func3(*args):
    print(type(args))
    return args 
print(func3())
print(func3(1,2))

def func4(**kwargs):
    print(type(kwargs))
    return kwargs 
print(func4())
print(func4(a=1, b=2))









