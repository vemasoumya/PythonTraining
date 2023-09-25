# Create a set of names
names_set = {"Amit", "Anika", "Bhavy", "Deepa", "Gagan", "Ishaa", "Karan"}

# Check if value is present in set
if "Deepa" in names_set:
    print("The name 'Deepa' is in the set.")
else:
    print("The name 'Deepa' is not in the set.")

# Add values to the set
names_set.add("Sarah")

# Removing Elements:
names_set.remove("Bhavy")
names_set.discard("NonExistentName")

# Print all the values of the set
for x in names_set:
    print(x)
