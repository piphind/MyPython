mondayTemperatures = [9.1, 8.8, 7.6, 5.2, 4.9, 3.2]
print("Interating round LISTS...")

print(round(mondayTemperatures[0]))
print(round(mondayTemperatures[1]))
print(round(mondayTemperatures[2]))
print(round(mondayTemperatures[3]))
print(round(mondayTemperatures[4]))
print(round(mondayTemperatures[5]))

# or
print("--- or ---")

for temperatures in mondayTemperatures:
    print(round(temperatures))

# Now for Dictionaries
print("Now for DICTIONARIES...")
student_grades = {"Mary": 9.1, "Simon": 8.8, "John": 7.5}

for grades in student_grades.items():
    print(grades)
