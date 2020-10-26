import datetime
# Simple Variable Types - These are implicit
# Result of a function
myNow = datetime.datetime.now()
# Number
myNumber = 10
# Text
myText = "Hello"
# Floating Point
myFloat = 3.1415
# Compound Variable Types
# List - MUTABLE
student_grades = [9.1, 8.8, 7.5]
# List using 'Range' and Step
listOne = list(range(1, 10))
listTwo = list(range(1, 10, 2))
# Dictionary
student_grades_dic = {"Mary": 9.1, "Simon": 8.8, "John": 7.5}
# Tuples - IMMtypeUTABLE
monday_temps = (13.6, 22.0, 9.0)

# Stuff you can do with LISTS
# Calculate the average using a couple of built-in functions
mySum = sum(student_grades)
length = len(student_grades)
mean = mySum / length

# Stuff you can do with DICTIONARIES
# Calculate the average using a couple of built in functions
mySum2 = sum(student_grades_dic.values())
length2 = len(student_grades_dic)
mean2 = mySum2 / length2

# Stuff you can do with TUPLES


# Display the variable values
print("The 'types' of the variables are ...", type(myNow), type(myNumber), type(myText), type(myFloat))
print("The date and time is ...", myNow)
print(myNumber)
print(myText)
print(myFloat)
print(student_grades)
print(listOne)
print(listTwo)
print(mean)
print(mean2)

