def mean(value):
    if isinstance(value, dict):
#   if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

student_grades1 = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(student_grades1))

student_grades2 = [9.1, 8.8, 7.5]
print(mean(student_grades2))

