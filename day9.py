class student:
    def __init__(self,name,age,branch,gpa):
        self.name=name
        self.age=age
        self.branch=branch
        self.gpa=gpa

    def introduce(self):
        print(f"name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Branch:{self.branch}")
        print(f"Gpa:{self.gpa}")
def study(self):
        print(f"{self.name} is studying in {self.branch}")

    def get_grade(self):
        if (self.gpa >=9.0):
            print(f"{self.name}'s Grade:A+")
        elif (self.gpa >=8.0):
            print(f"{self.name}'s Grade:A")
        elif (self.gpa >=7.0):
            print(f"{self.name}'s Grade:B")

student1 =student("kiyo",20,"csm",8.5)
student2 =student("kiyomi",21,"cse",8.9)
student1.introduce()
student1.study()
student1.get_grade()

student2.introduce()
student2.study()

        

        
