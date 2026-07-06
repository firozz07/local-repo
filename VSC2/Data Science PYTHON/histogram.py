import matplotlib.pyplot as plt
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
plt.hist(marks, bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

hours_studied = [1, 2, 3, 4, 5, 6, 7]
marks = [35, 40, 50, 55, 65, 75, 85]
plt.scatter(hours_studied, marks, color='red')
plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()