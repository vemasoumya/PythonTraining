#key value pairs
#key is immutable and values are mutable 
# Create a dictionary
# no order 
person = {"name": "John", "age": 30, "city": "New York"}

#how to access dictory values using key
name = person["name"]
print(name)
print(person.get("age"))


# Add new value
person["occupation"] = "Engineer"

#modify a value
person["age"] = 31 
print(person)

#remove keyvalue pair
del person["occupation"] 
#person.pop("occupation")
#person.pop("occupation", None)
print(person)

#iterate through key values 

for key, value in person.items():
    print (f"{key}: {value}")

#iterate through values only
for items in person.values():
    print(items)


#work with list of dictionaries

people = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Alice", "age": 25, "city": "Los Angeles"},
    {"name": "Bob", "age": 35, "city": "Chicago"}
]

# Accessing values for specific people
john_name = people[0]["name"]
alice_age = people[1]["age"]

multi_dict = {"name": "John", "age": 30, "city": "New York", "1" : [1,2,3,4]}


