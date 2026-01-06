import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv(r"DataHandlingPractice\employee.csv")

print(df.isnull().sum())

# Features & Target
X = df[['Age','Experience','Education']]
y = df['Salary']

# Scaling ONLY X
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=40
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Evaluation
print("MAE:", mean_absolute_error(y_test, pred))
print("R2:", r2_score(y_test, pred))

# New employee prediction
new_emp = scaler.transform([[27,4,16]])
print("Predicted Salary:", model.predict(new_emp))
