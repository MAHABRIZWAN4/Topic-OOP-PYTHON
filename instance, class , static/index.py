class Student:
    school = "The Smart School"

    def __init__(self, name):
        self.name = name

    def show_name(self):  # Instance method
        print("Student ka naam:", self.name)

    @classmethod
    def show_school(cls):  # Class method
        print("School ka naam:", cls.school)

    @staticmethod
    def greet():  # Static method
        print("Hello! Welcome to school.")


s1 = Student("Areeba")
s1.show_name()       # Instance method
Student.show_school()  # Class method
Student.greet()        # Static method


