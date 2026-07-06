import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# Dataset
data = {
'Hours':[1,2,3,4,5,6,7,8],
'Scores':[15,25,35,45,55,65,75,85]
}
df = pd.DataFrame(data)
# Independent and Dependent variables
X = df[['Hours']]
y = df['Scores']
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=0
)
# Create model
model = LinearRegression()
# Train model
model.fit(X_train, y_train)
# Predict test values
y_pred = model.predict(X_test)
print("Predicted Scores:", y_pred)
# Predict new value
prediction = model.predict([[9]])
print("Predicted Score for 9 hours:", prediction[0])
# Plot graph
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel("Study Hours")
plt.ylabel("Student Scores")
plt.title("Simple Linear Regression")
plt.show()
