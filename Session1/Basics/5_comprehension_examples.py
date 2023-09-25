#easy logic to generate elements in the list

# A comprehension is a concise and readable way to create lists, dictionaries, or sets


l1 = [num**2 for num in range(1,100)]
print(l1)
l2 = [char for char in "SoumyaVema" if char.lower() in ['a','e','i'] ]
print(l2)

dict1 = {p : p * p for p in range(1,11) if p%2 == 0}
print(dict1)
sample_dict = {'a' :1, 'b' : 2}
dict2 = { key:value * 2 for key,value in sample_dict.items() }
print(dict2)



