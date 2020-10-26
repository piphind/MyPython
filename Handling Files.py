myfile = open("fruits.txt")
print(myfile.read())
myfile.close()

# Or use this syntax
with open("fruits.txt") as myfile:
    content = myfile.read()
print(content)

# Writing to a file ....
with open("vegetables.txt", "w") as myfile:
    myfile.write("Tomato")

# Appending to a file (does not allow read) ...
with open("vegetables.txt", "a") as myfile:
    myfile.write("\nOkra")

# Appending to a file (reposition to then read) ...
with open("vegetables.txt", "a+") as myfile:
    myfile.write("\nOkra")
    myfile.seek(0)
    content = myfile.read()
print(content)
