#Encapsulation = settig limits and protecting data inside a class 
class Student:
    def __init__(self, name, gpa):
        self.name = name 
        self.__gpa = gpa  # private attribute

    def get_gpa(self): 
        return self.__gpa  # public method to access private attribute
    
    def set_gpa(self, new_gpa):
        if new_gpa < 0 or new_gpa > 10:
            print("Invalid GPA. Please enter a value between 0 and 10.")
        else:
            self.__gpa = new_gpa  # public method to modify private attribute

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"  GPA : {self.__gpa}")

kiyo = Student("kiyo", 7)
kiyo.introduce()

print(kiyo.get_gpa())

kiyo.set_gpa(9)
# kiyo.set_gpa(504)
kiyo.introduce()
