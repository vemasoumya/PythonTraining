# attributes and methods (Encapsulation)
class PlayerCharacter:
    #class object attribute
    #common for all objects
    membership = True 
    def __init__(self, name='anonymous', age=10):
        if age > 10:
            self.name = name
            self.age = age 

    def run(self):
        print(f'my name is {self.name} and I am {self.age} years old')
        print(f'my membership is {PlayerCharacter.membership}')
        print(f'my membership is {self.membership}')
        return 'done'
    
    #we use class method when we want to modify class attributes
    @classmethod
    def adding_numbers(cls, num1, num2):
        print("Class method")
        return num1 + num2 
        #return cls('Ravi', num1+num2 )

    #we dont care about Class state/attributes 
    @staticmethod
    def adding_numbers_new(num1, num2):
        print("static method")
        return num1 + num2
    
player1 = PlayerCharacter("Rahul", 20)
print(player1)
player1.run()
# player2 = PlayerCharacter("Raj", 20)
# player2.run()
# player3 = PlayerCharacter()
# print(player3)
# player3.run()
# print("testing class method")
# print(PlayerCharacter.adding_numbers(10,12) )
#print(PlayerCharacter.adding_numbers_new(1,1))