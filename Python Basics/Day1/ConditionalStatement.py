# Take input from user:

# Name

# Age

# Blood Pressure (systolic)

# Symptom (fever, cough, none)

# Use if-elif-else to give advice:

# Age < 18 → "Minor: Consult pediatrician"

# Age 18–60 → "Adult: Consult general physician"

# Age > 60 → "Senior: Consult geriatric specialist"

# BP > 140 → "High blood pressure: Immediate checkup"

# Symptom = fever → "Possible infection: Take test"

# Use nested conditions for combined checks:

# Example: Adult + BP > 140 → "Adult with high BP: Consult cardiologist"

Name_Of_Patient = input("Enter patient name: ")
Age = int(input("Enter patient age: "))
BloodPressure = int(input("Enter blood pressure of a patient: "))
Symptom = input("Enter your symptoms: ")

if(Age < 18):
    print("Monor: Consult pediatrician.")

elif(18 <= Age <=60):
    print("Senior: Consult geriatric specialist.")

elif BloodPressure > 140:
    print("High blood pressure. Check immediately")

    if Age < 60:
        print("Immediately go hospital")



if Symptom.lower() == "fever":
    print("may be something") 
elif Symptom.lower() == "cough":
    print("May be cold: Monitor symptoms")
else:
    print("No specific symptom reported")            
