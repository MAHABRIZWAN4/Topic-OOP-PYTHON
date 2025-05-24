# 🔹 3. Static Method (General kaam - kisi pe depend nahi karta)
# 📖 Kya hota hai?
# Jab aap koi aisa kaam kar rahe ho jo na object pe depend karta hai na class pe — bas ek general kaam hota hai.

# 🔑 Isme self ya cls nahi hota.

class Student:
    @staticmethod
    def add(x, y):  # Static method
        print("Addition:", x + y)


Student.add(3, 4)  # Output: Addition: 7


# 🧃 Daily life example:
# Jaise calculator app mein 2 + 3 karna. Ye kisi student ka data nahi, bas general kaam hai.
# To ye static method hota hai.