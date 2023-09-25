class Toy():
    def __init__(self, age, color):
        self.age = age 
        self.color = color 
    
    def __str__(self):
        return self.color 
    
figure = Toy(10, "Red")
print(str(figure))
print(figure.__str__())
print("test".__str__())