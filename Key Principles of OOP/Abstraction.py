# Abstraction in Python

from abc import ABC, abstractmethod
class Auth(ABC):
    @abstractmethod
    def Login():
        pass



class LoginPassword(Auth):
     def Login(self, email, password):
        print("LOGIN SUCCESSFULLY")

l1 = LoginPassword()
l1.Login(email="mahab@gmail.com",password="1234")




class LoginGoogle(Auth):
    def Login(self):
        print("Redirecting to Google for authentication...")
        print("LOGIN SUCCESSFULLY via Google")
g = LoginGoogle()
g.Login()



class LoginFacebook(Auth):
    def Login(self):  
        print("Redirecting to Facebook for authentication...")
        print("LOGIN SUCCESSFULLY via Facebook")

fb = LoginFacebook()
fb.Login()





# Abstract class another example
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Internal complex system
class EngineSystem:
    def inject_fuel(self):
        print("Fuel injected.")

    def spark_plug(self):
        print("Spark plug fired.")

    def move_pistons(self):
        print("Pistons moving.")

# Concrete class
class Car(Vehicle):
    def __init__(self):
        self.engine = EngineSystem()

    def start_engine(self):
        # Complex steps (hidden from user)
        self.engine.inject_fuel()
        self.engine.spark_plug()
        self.engine.move_pistons()
        print("Car engine started successfully.")

# User code
my_car = Car()
my_car.start_engine()







# Abstract class example
class Person(ABC):
    def greet(self):
        print("Hello, welcome!")

    @abstractmethod
    def work(self):
        pass

class Teacher(Person):
    def work(self):
        print("I teach students.")

# Object banate hain
t = Teacher()
t.greet()
t.work()





# Abstract class example
class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def do_work(self):
        pass

class Developer(Employee):
    def do_work(self):
        print(f"{self.name} is writing code.")

# Object banate hain
dev = Developer("Mahab", 101)
dev.do_work()





# Abstract class example
from rich import print
class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._engine_status = False
        self._idling_time = 0
        self._traffic_signal = None

# Expose a drive method without revealing internal mechanics
    def drive(self):
        if self._engine_status and self._traffic_signal=="green":
            print("You are driving a {self.brand} {self.model}")
        elif self._traffic_signal=="red":
            print(f"You stopped at the red light in a {self.brand} {self.model}.")
            self._idle_stop_engine()
        else:
            self._start_engine()
            print(f"You are driving a {self.brand} {self.model}.")


# Expose a stop method to stop the car
    def stop(self):
        if self._engine_status:
            print(f"You stopped the {self.brand} {self.model}.")
            self._idle_stop_engine()
        else:
            print(f"The {self.brand} {self.model} is already stopped.")

    # Expose a set_traffic_signal method to set the traffic signal
    def set_traffic_signal(self, signal):
        self._traffic_signal = signal
        if signal == "red":
            print(f"Traffic signal turned red. You stopped in a {self.brand} {self.model}.")
            self._idle_stop_engine()
        elif signal == "green":
            print(f"Traffic signal turned green. You can drive your {self.brand} {self.model}.")
            if not self._engine_status:
                self._start_engine()

    # Internal method to start the engine (hidden from user)
    def _start_engine(self):
        self._engine_status = True
        self._idling_time = 0
        print("Engine started.")

    # Internal method to stop the engine if idling for 5 seconds (hidden from user)
    def _idle_stop_engine(self):
        import time
        print("Engine is idling...")
        for i in range(5):
            print(f"Idling time: {i+1} seconds")
            time.sleep(1)
            self._idling_time += 1
        if self._idling_time >= 5:
            self._engine_status = False
            print("Engine stopped (idle stop) to save fule.")



# Create a Car object and use the methods
my_car = Car("Toyota", "Camry")
my_car.set_traffic_signal("green")
my_car.drive()
my_car.set_traffic_signal("red")
my_car.set_traffic_signal("green")
my_car.drive()

