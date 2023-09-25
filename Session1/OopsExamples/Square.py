

class Rectangle(object):
    def __init__(self, l, b):
        self.length = l 
        self.breadth = b
        print("super class constructor called")       

    def display_info(self):
        print("I am a rectangle")

    # def get_perimiter(self):
    #     return 2 * self.length + 2 * self.breadth 
    
    def get_area(self):
        return self.length * self.breadth 

class Square(Rectangle):
    def __init__(self,l):
        self.length = l
        #we can refer to a parent class with the use of super() function 
        # inside the inherited or child class
        #The super() function we use in the child class returns a temporary created object of the superclass,
        # that allow us to access all of its method present in the child class.
        super().__init__(l,l)        
        print("sub class constructor called")

    def display_info(self):
        print("I am a square")

square = Square(4)
square.display_info()
#print(square.get_perimiter())
print(square.get_area())
#print(dir(square))
#print(square)
#print(str(square))
#print(square.__str__())





    
