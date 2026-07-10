class student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"GPA: {self.gpa}")

kiyo = student("kiyo", 20, 9)

class mlstudent(student):
    def __init__(self, name, age, gpa, research_topic):
        super().__init__(name, age, gpa)
        self.research_topic = research_topic

    def display(self):
        super().display()
        print(f"Research Topic: {self.research_topic}")


kiyo = mlstudent("kiyo", 20, 9, "DBMS")
kiyo.display()
