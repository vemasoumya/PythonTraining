class Car:
    def __init__(self,x1):
        self.x1 = x1

    def start(self):
        print("start the car")

    def go(self):
        print('Going', self.x1)

class Flyable:
    def __init__(self,x2):
        self.x2 = x2

    def start(self):
        print("start the flyable")

    def fly(self):
        print('Flying', self.x2)

class FlyingCar(Car, Flyable):
    #pass
    def __init__(self, x3,x4):
        Flyable.__init__(self,x3)
        Car.__init__(self,x4)

fc1 = FlyingCar(5,10)
print(FlyingCar.__mro__)
print(FlyingCar.mro())
# fc1.start()
# fc1.fly()
# fc1.go()