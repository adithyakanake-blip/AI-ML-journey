import matplotlib.pyplot as plt
x = ['mon','tue','wed','thu','fri','sat','sun']
y = [170, 180, 160, 200, 210, 190, 220]
plt.scatter(x, y, color='red', marker='D',alpha=0.5)
plt.xlabel('Days')
plt.ylabel('Values')
plt.title('Scatter Plot')
plt.show()