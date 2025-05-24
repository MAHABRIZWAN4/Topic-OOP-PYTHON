# Inheritance in Python

class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed


    def drive(self):
         print("Driving Speed = ", self.speed)

    def accelerate(self):
        self.speed += 10

# Car inherits from Vehicle  
class Car(Vehicle):
    def __init__(self, color, speed, model):
        super().__init__(color, speed)
        self.model = model




# Bike inherits from Car  
class Bike(Car):
    def __init__(self, color, speed, model, bike_type):
        super().__init__(color, speed, model)
        self.bike_type = bike_type




v1 = Vehicle("Red",30)
print(v1.color)
print(v1.speed)
v1.drive()
v1.accelerate()
print(v1.speed)



c1 =  Car("Yellow",40,"r3")
print(c1.color)
print(c1.speed)
print(c1.model)


b1 = Bike("Blue",50,"r1","mountain")
print(b1.color)
print(b1.speed)
print(b1.model)
print(b1.bike_type)
b1.drive()
b1.accelerate()
print(b1.speed)