class loops:
    def __init__(self):
        print("initialize constructor")

###############################################for loop###############################################

#for loops with list 

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#for loops with tuple

fruits = ("papya", "pineapple", "watermalen")
for fruit in fruits:
    print(fruit)

#for loops with dictionary

person ={"name" :"Ajay", "age" : 30, "city": "Hyderabad"}

for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)


###############################################for loop###############################################

colors = ("red", "green", "blue")
index = 0
while index <len(colors):
    print(index,colors[index])
    index +=1


person = {"name": "Alice", "age": 30, "city": "New York"}
keys = list(person.keys())
index = 0
while index < len(keys):
    print(keys[index])
    index +=1
