# 🔐 Getter & Setter Methods – Simple Definition
# ✅ Getter:
# Data lene ke liye hota hai (value read karne ke liye).

# ✅ Setter:
# Data set karne ke liye hota hai (value change/update karne ke liye).

# 💬 Daily Life Example:
# Agar fridge lock hai (private), to aap direct andar se saman nahi nikaal sakte.
# Aapko key (getter) se dekhna padega kya rakha hai, aur permission (setter) se naya saman rakhna hoga.



class Student:
    def __init__(self):
        self.__marks = 0  # Private attribute

    def get_marks(self):     # Getter
        return self.__marks

    def set_marks(self, value):  # Setter
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks!")

s1 = Student()
s1.set_marks(85)          # Setter
print(s1.get_marks())     # Getter
# 🎯 Real-Time Example:
# Mobile App: Aap apna password dekh nahi sakte (private), lekin "show password" ka button hota hai (getter).

# Jab aap naya password daalte ho, app check karta hai strong hai ya nahi (validation) — ye hota hai setter.
