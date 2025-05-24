# 🔧 1. Constructor (__init__)
# Matlab: Jab koi naya object banta hai, to us waqt chalne wala function.

# Daily Life Example: Jab aap naye bartan le kar aate ho (object), to unhein dhona padta hai (tayyar karna hota hai). To __init__ usi kaam ko karta hai — object ko tayyar karta hai.




# 🧹 2. Destructor (__del__)
# Matlab: Jab object ka kaam khatam ho jata hai ya use delete kar diya jata hai, to us waqt chalne wala function.

# Daily Life Example: Jaise hi aap chai pee lete ho, cup ko dhona hota hai ya dustbin mein daalna hota hai — __del__ ye kaam karta hai.



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"{self.brand} {self.model} car ban gayi hai!")

    def __del__(self):
        print(f"{self.brand} {self.model} car delete ho gayi hai!")

# Object create karna
my_car = Car("Toyota", "Corolla")  # Constructor chalega

# Object delete karna
del my_car  # Destructor chalega



