Names = ["Amit","Anika","Bhavy","Deepa","Gagan","Ishaa","Karan"]
Names2 =  ["get","Bet"]
# get the length of list 
print(len(Names))

#print 3rd item in the index from the list
print(Names[2])

#Add new name in the list
Names.append("testing")
print(Names)

#Add new name using insert function
Names.insert(3,"indextesting")
print(Names)

# Add another list
Names.extend(Names2)
print(Names)

#Remove element by name
Names.remove("indextesting")
print(Names)

#Remove element by name
Names.pop(5)
print(Names)

#clean entire list
#Names2.clear()
print(Names2)

#change any value in the list
Names2[1] ="tokyo"
print(Names2)