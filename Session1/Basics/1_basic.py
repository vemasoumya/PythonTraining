
#Interpreted language

temp = 60
if temp == 10:
    print("fine")

#ndentation Matters


temp = 60
if temp == 10:
    print(temp)
#print("fine")

#multi line comment
"""
a = 1
b = 2
"""

#dynamic typed language
x = 5
y = 3.45
name = "Alice"

print(x)
print(y)
print(name)

#changing Variable type 
age = 25
print(age)  # age is an integer

age = "Twenty-five"
print(age)  # age is now a string


#String small changes 

#Concatenation

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  
print(result)

#String Length:
text = "Python is great!"
length = len(text)
print("Length:", length)

#String Formatting:
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)


# :- Slice Operator
# name = 'microsoft'

#   +---+---+---+---+---+---+---+---+---+
#   | m | i | c | r | o | s | o | f | t |
#   +---+---+---+---+---+---+---+---+---+
#   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
#   +---+---+---+---+---+---+---+---+---+
#   |-9 |-8 |-7 |-6 |-5 |-4 |-3 |-2 |-1 |
#   +---+---+---+---+---+---+---+---+---+

# print(name[2:5])
# print(name[2:])
# print(name[:5])
# print(name[-3:])
# print(name[:-5])
# print(name[::-1])
# print(name[::-3])
# print(name[::3])
# print(name[-7::])