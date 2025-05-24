# Encapsulation in Python
class Car:
    def __init__(self, color, speed):
        self.color = color  # Public attribute
        self.__speed = speed  # Private attribute (encapsulated)

    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed
    

Car1 = Car("red", 50)
print(Car1.color)  # Accessing public attribute
#print(Car1.__speed)  # This will raise an AttributeError
print(Car1.get_speed())  # Accessing private attribute via public method

Car1.accelerate()  # Check speed after acceleration
print(Car1.get_speed())  # Accessing private attribute via public method



