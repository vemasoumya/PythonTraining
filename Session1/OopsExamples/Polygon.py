

class Polygon(object):
    def __init__(self, sides):
        self.sides = sides  
        print("super class constructor called")      

    def display_info(self):
        print("Polygon is multi dimensional")

    def get_perimiter(self):
        return sum(self.sides)

class Triangle(Polygon):

    def display_info(self):
        print("Triangle is a polygon with 3 sides")

class Square(Polygon):

    def display_info(self):
        print("Square is a polygon with 3 sides")

polygon = Polygon([4,4,4,4])
triangle = Triangle([3,4,5])
square = Square([4,4,4,4])
print(isinstance(triangle, Triangle))
print(isinstance(triangle, Polygon))
print(isinstance(triangle, object))
for obj in [polygon, triangle, square ]:
       obj.display_info()
       print("Perimeter", obj.get_perimiter())
    
