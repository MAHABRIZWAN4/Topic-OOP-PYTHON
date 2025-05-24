# 🔹 2. Class Method (Class ka kaam - sab ke liye)
# 📖 Kya hota hai?
# Agar aapko poori class ke data ke sath kaam karna ho (jo har object ke liye same ho), to aap class method use karte ho.

# 🔑 Pehla parameter: cls
# cls ka matlab hota hai ye wali class.


class Student:
    school = "The Smart School"

    @classmethod
    def show_school(cls):  # Class method
        print("School ka naam hai:", cls.school)



Student.show_school()  # Output: School ka naam hai: The Smart School



# 🧃 Daily life example:
# Aapke school ka naam har student ke liye same hota hai. To agar koi pooche "aap kis school mein ho?" to sab ka answer same hoga.

# Ye hai class method — sab objects ke liye common baat.



