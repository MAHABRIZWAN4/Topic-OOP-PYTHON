# 🔹 1. Instance Method (Object ka kaam)
# 📖 Kya hota hai?
# Jab hum class ka object banate hain (jaise ek student), to har object ke apne alag data hote hain (name, age, etc).
# Instance method sirf usi object ke data ke saath kaam karta hai.

# 🔑 Pehla parameter: self
# self ka matlab hota hai ye wala object.


class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):  # Instance method
        print("Student ka naam hai:", self.name)

s1 = Student("Ali")
s1.show_name()  # Output: Student ka naam hai: Ali
# 🧃 Daily life example:
# Jaise har student ka apna bag hota hai. Agar aap Ali ka bag dekh rahe ho, to usi ka bag open hoga — kisi aur ka nahi.
# Ye hai instance method — har object ka alag kaam.