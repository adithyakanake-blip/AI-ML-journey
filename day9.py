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
student1 =student("kiyo",20,"csm",8.5)
student2 =student("kiyomi",21,"cse",8.9)
student1.introduce()
student2.introduce()


        