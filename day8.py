#Day_7 - Mini project : Student Grade calculator + File Handling
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


REPORT_FILE = "student_reports.txt"


#student ka report - ab file mein bhi save hoga
def student_report(student):
    marks = student["Marks"]
    total = sum(marks)
    avg = total/len(marks)
    grade = grade_calculator(avg)
    status = Status(avg)

    #report ko ek string mein banate hai, taki print aur file dono mein use ho sake
    lines = []
    lines.append("*"*40)
    lines.append("STUDENT REPORT CARD")
    lines.append("*"*40)
    lines.append(f"Name:{student['Name']}")
    lines.append(f"Branch:{student['Branch']}")

    for i in range(len(student["subjects"])):
        sub_name = student["subjects"][i]
        mark_value = student["Marks"][i]
        lines.append(f"{sub_name}:{mark_value}")

    lines.append(f"Total:{total}")
    lines.append(f"Average:{avg}")
    lines.append(f"Grade:{grade}")
    lines.append(f"Status:{status}")
    lines.append("")  #blank line - next report se gap ke liye

    report_text = "\n".join(lines)

    #screen par print karo
    print(report_text)

    #file mein save karo (append mode - purane records delete nahi honge)
    try:
        with open(REPORT_FILE, "a") as f:
            f.write(report_text + "\n")
        print(f"(Report saved to {REPORT_FILE})")
    except IOError:
        print("Error: report file mein save nahi ho paya!")


#saare saved reports ko file se padh kar dikhao
def view_all_reports():
    try:
        with open(REPORT_FILE, "r") as f:
            content = f.read()
            if content.strip() == "":
                print("\nAbhi tak koi report save nahi hui hai.")
            else:
                print("\n" + "="*40)
                print("ALL SAVED REPORTS")
                print("="*40)
                print(content)
    except FileNotFoundError:
        print("\nAbhi tak koi report file exist nahi karti. Pehle ek student ka report banao.")


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
        #exit karne se pehle saare records dekhne ka option
        view_choice = input("\nDo you want to view all saved reports? (yes/no): ")
        if view_choice.lower() == "yes":
            view_all_reports()
        print("\nTHANK YOU")

main()