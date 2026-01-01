
# Worker Salary & Bonus Predictor


import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score


# Step 1: Load Data

df = pd.read_csv("workers_full_data.csv")

# Preview
print("Original Data:")
print(df.head())
print(df.info())

# Step 2: Handle Missing Values
df = df.replace([""," ", "NaN","Nan","nan","None","No"], pd.NA)

# Fill missing city with forward fill
df['City'].fillna(method='ffill', inplace=True)

# Daily Work Hours numeric + fill missing
df['Daily_Work_Hours'] = pd.to_numeric(df['Daily_Work_Hours'], errors='coerce')
df['Daily_Work_Hours'].fillna(df['Daily_Work_Hours'].mean(), inplace=True)

# Fill missing Salary with mean
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# ------------------------------
# Step 3: Encode Categorical Columns
# ------------------------------
# Gender encoding
df['Gender_Encode'] = LabelEncoder().fit_transform(df['Gender'])

# One-hot encode City and Department
df = pd.get_dummies(df, columns=['City','Department'], drop_first=False)

# Drop original Gender
df.drop(columns=['Gender'], inplace=True)

# ------------------------------
# Step 4: Scale Numeric Columns
# ------------------------------
scaler = StandardScaler()
df[['WorkerID_Scale','Experience_Years_Scale','Daily_Work_Hours_Scale']] = scaler.fit_transform(
    df[['WorkerID','Experience_Years','Daily_Work_Hours']]
)

# ------------------------------
# Step 5: Analysis
# ------------------------------
print("\nAverage Salary by Department:")
dept_cols = [col for col in df.columns if 'Department' in col]
for dept in dept_cols:
    avg_salary = df[df[dept]==1]['Salary'].mean()
    print(f"{dept}: {avg_salary:.2f}")

print("\nTotal Work Hours by City:")
city_cols = [col for col in df.columns if 'City' in col]
for city in city_cols:
    total_hours = df[df[city]==1]['Daily_Work_Hours'].sum()
    print(f"{city} Total Hours: {total_hours}")

# Workers eligible for bonus (>8 hours/day)
df['Bonus_Eligible'] = np.where(df['Daily_Work_Hours'] > 8, 1, 0)
print("\nWorkers Bonus Eligibility:")
print(df[['WorkerID','Daily_Work_Hours','Bonus_Eligible']])

# ------------------------------
# Step 6: Linear Regression - Predict Salary
# ------------------------------
# Features for Salary prediction
X_salary = df.drop(columns=['Salary','Bonus_Eligible'])
y_salary = df['Salary']

# Split
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_salary, y_salary, test_size=0.3, random_state=42)

# Train model
lin_model = LinearRegression()
lin_model.fit(X_train_s, y_train_s)

# Predict on test
y_pred_s = lin_model.predict(X_test_s)
print("\nLinear Regression - Salary Prediction")
print("MSE:", mean_squared_error(y_test_s, y_pred_s))
print("Predicted salaries:", y_pred_s[:5])

# ------------------------------
# Step 7: Logistic Regression - Predict Bonus Eligibility
# ------------------------------
# Features for Bonus prediction
X_bonus = df.drop(columns=['Salary','Bonus_Eligible'])
y_bonus = df['Bonus_Eligible']

# Split
X_train_b, X_test_b, y_train_b, y_test_b = train_test_split(X_bonus, y_bonus, test_size=0.3, random_state=42)

# Train model
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train_b, y_train_b)

# Predict
y_pred_b = log_model.predict(X_test_b)
acc = accuracy_score(y_test_b, y_pred_b)
print("\nLogistic Regression - Bonus Prediction")
print("Accuracy:", acc)
print("Predicted Bonus Eligibility:", y_pred_b[:5])

# ------------------------------
# Step 8: Predict New Worker
# ------------------------------
# Example new worker
new_worker = pd.DataFrame(columns=X_salary.columns)
new_worker.loc[0] = 0  # fill 0 for all columns

# Fill features
new_worker.at[0,'Gender_Encode'] = 1          # Male
new_worker.at[0,'City_Kathmandu'] = 1
new_worker.at[0,'Department_IT'] = 1
new_worker.at[0,'WorkerID_Scale'] = 0
new_worker.at[0,'Experience_Years_Scale'] = scaler.transform([[0,5,8]])[0][1]
new_worker.at[0,'Daily_Work_Hours_Scale'] = scaler.transform([[0,5,8]])[0][2]

# Predict salary
pred_salary = lin_model.predict(new_worker)[0]

# Predict bonus eligibility
pred_bonus = log_model.predict(new_worker)[0]

print("\nNew Worker Prediction:")
print(f"Predicted Salary: {pred_salary:.2f}")
print(f"Bonus Eligibility: {'Yes' if pred_bonus==1 else 'No'}")

# ------------------------------
# Step 9: Save Cleaned Data
# ------------------------------
df.to_csv("workers_cleaned.csv", index=False)
print("\nCleaned data saved as 'workers_cleaned.csv'")
