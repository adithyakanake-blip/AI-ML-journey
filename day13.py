import matplotlib.pyplot as plt

# Your data
subjects = ["Python", "ML", "Data Structures", 
            "Maths", "English"]
marks = [85, 92, 78, 95, 88]

# BAR CHART


# method 1: Using plt.bar() function

# plt.figure(figsize=(10, 6))
# plt.bar(subjects, marks, color="purple")
# Add value labels on top of each bar!

# method 2: Using plt.bar() function with value labels


for i, mark in enumerate(marks):
    plt.text(i, mark + 0.5, str(mark), 
             ha='center', fontweight='bold')

# Add grid for readability
plt.grid(axis='y', alpha=0.3)

# Change color to show performance
colors = ['green' if m >= 90 else 'orange' 
          if m >= 80 else 'red' for m in marks]
plt.bar(subjects, marks, color=colors)
plt.title("Marks in Different Subjects")      
plt.xlabel("Subjects")    
plt.ylabel("Marks")     
plt.show()