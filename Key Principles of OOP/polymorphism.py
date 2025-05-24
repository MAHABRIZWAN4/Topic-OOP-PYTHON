# Polymorphism in Python

# Polymorphism ka matlab hota hai:

# Aik hi kaam, lekin har shakhs ya cheez ka apna apna tareeqa.



# Example: "Bolna" (Speak karna)
# Teacher bolti hain: Taleem deti hain

# Doctor bolta hai: Patients ko mashwara deta hai

# Baby bolta hai: Rota hai ya cute awaz nikalta hai


# EXAMPLE 1 
class Teacher:
    def speak(self):
        print("Teacher : Main taleem day rahi hoon.")

class Doctor:
    def speak(self):
        print("Doctor : Main patient ko mashwara day raha hoon.")

class Baby:
    def speak(self):
        print("Baby : Main ro raha hoon.")

def call_speak(person):
    person.speak()


# Objects
t = Teacher()
d = Doctor()
b = Baby()



call_speak(t)   # Output: Main taleem day rahi hoon.
call_speak(d)   # Output: Main patient ko mashwara day raha hoon.
call_speak(b)   # Output: Main ro raha hoon.




# EXAMPLE 2
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> None:
        pass

class Dog(Animal):
    def speak(self) -> None:
        print(type(self), ":  Woof!")

class Cat(Animal):
    def speak(self) -> None:
        print(type(self), ":  Meow!")

def animal_sound(animal: Animal) -> None:
    animal.speak()

dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!


