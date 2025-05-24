## 🔸 **1. Composition (Strong "has-a" relationship)**

### 📖 Simple Definition:

# Ek object ke andar doosra object hota hai, aur **agar outer object delete ho jaye, to andar wala bhi khatam** ho jata hai.

### 🔧 Daily Life Example:

# **Car aur Engine**
# Agar car destroy ho jaye, to uska engine bhi kaam ka nahi rahta — engine sirf car ke sath hi chalta hai.



### 💻 Code Example:

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start_car(self):
        self.engine.start()

my_car = Car()
my_car.start_car()  # Output: Engine started.


### 🧠 Real-time Example:

# Mobile aur uska battery — agar mobile destroy ho gaya, to battery kaam nahi karegi.


## 🔹 **2. Aggregation (Weak "has-a" relationship)**

### 📖 Simple Definition:

# Ek object doosre object ko use karta hai, **lekin dono alag bhi reh sakte hain**.

### 🏫 Daily Life Example:

# **University aur Departments**
# University khatam ho jaye to department kisi aur university mein shift ho sakta hai — **independent** hai.



### 💻 Code Example:

class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, dept):
        self.department = dept  # Aggregation

    def show_dept(self):
        print("Department:", self.department.name)


dept1 = Department("Computer Science")
uni = University(dept1)
uni.show_dept()  # Output: Department: Computer Science


### 🧠 Real-time Example:

# Teacher aur School — agar school band ho jaye, teacher kisi aur school mein jaa sakta hai.



## 📊 **Comparison Table (Simple Roman Urdu):**

# | Feature        | Composition                   | Aggregation                      |
# | -------------- | ----------------------------- | -------------------------------- |
# | Relationship   | Strong (depends completely)   | Weak (independent reh sakta hai) |
# | Example        | Car has-a Engine              | University has-a Department      |
# | If outer dies? | Inner bhi destroy ho jata hai | Inner phir bhi zinda rehta hai   |
# | Code           | Object create inside class    | Object pass from outside         |

