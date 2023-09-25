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