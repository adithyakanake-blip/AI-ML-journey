#Day_6 - Mini project : Student Grade calculator
def grade_calculator(avg):
    if avg >=90:
        return "A+"
    elif avg >=80:
        return "A"
    elif avg >=70:
        return "B"
    elif avg >=60:
        return "C"
    elif avg >=50:
        return "D"
    else:
         return"F - need improvement"

#pass/fail
def Status(avg):
    if avg >=90:
        return "Great"
    elif avg >=80:
        return "Good"
    elif avg >=70:
        return "Well done"
    elif avg >=60:
        return "PASS with distinction"
    elif avg >=50:
        return "PASS"
    else:
        return " CANDIDATE FAILED"



#student ka report
def student_report(student):
    marks =student["Marks"]
    total = sum(marks)
    avg = total/len(marks)
    grade = grade_calculator(avg)
    status = Status(avg)
    print("*"*40)
    print(f"STUDENT REPORT CARD")
    print("*"*40)   
    print(f"Name:{student["Name"]}")
    print(f"Branch:{student["Branch"]}")

    for i in range(len(student["subjects"])):
        sub_name =student["subjects"][i]
        mark_value =student["Marks"][i]
        print(f"{sub_name}:{mark_value}")

    print(f"Total:{total}")
    print(f"Average:{avg}")
    print(f"Grade:{grade}")
    print(f"Status:{status}")


def main():
    print(f"STUDENT REPORT CARD")
    print("-"*20)


    name = input(f"Enter student name:")
    branch = input(f"Enter branch name:")


    subjects =["Python programming","Data structure","mathematics","OOPS in Java","ML"]
    marks =[]
    print("Enter marks out of 100:")
    for subjects in subjects:
        while True:
            try:
                mark =float(input("Enter the marks:"))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("please the valid marks 0-100!")
            except ValueError:
                    print("Enter a valid number")

    student ={
                "Name": name,
                "Branch": branch,
                "subjects":["Python programming","Data structure","mathematics","OOPS in Java","ML"],
                "Marks":marks
                }
    student_report(student)

    new_student =input("\n calculate for new student? (yes/no)")
    if new_student.lower()=="yes":
        main()
    else:
        print("\nTHANK YOU")

main()