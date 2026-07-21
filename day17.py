import matplotlib.pyplot as plt 
plt.style.use("fivethirtyeight")
students = [50,47,42,34,44]
labels =['CSE','CSE(AIML)','CIVIL','MECH','CSD']
explode =[0,0.1,0,0,0]

plt.pie(students,labels=labels,explode=explode,shadow=True,autopct='%1.1f%%'
        ,startangle=90,wedgeprops={'edgecolor':'black'})

plt.title("no.of students in class")
plt.tight_layout()
plt.show()