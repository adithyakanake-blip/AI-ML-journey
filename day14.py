import matplotlib.pyplot as plt
# LINE CHART
semesters = [1, 2, 3, 4, 5, 6]
gpa =       [7.2, 7.8, 8.1, 8.5, 8.9, 9.2]

plt.figure(figsize=(10, 6))
plt.plot(semesters, gpa, color="blue", 
         marker="o", linewidth=2)
plt.title("GPA Progress Over Semesters")
plt.xlabel("Semesters")
plt.ylabel("GPA")
plt.grid(True)
plt.show()