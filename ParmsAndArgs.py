# Function with non-default parameters
def calcarea1(a, b):
    return a*b


# Function with default parameters (these must come after any non-default parameters)
def calcarea2(a, b=5):
    return a*b


# Function with an arbitrary number of non-keyword parameters
def mean(*args):
    return sum(args) / len(args)


# Function with an arbitrary number of keyword parameters
def func1(**kwargs):
    return kwargs



# Call the function with non-keyword (positional) arguments
print(calcarea1(5, 5))

# Call the function with keyword arguments
print(calcarea1(a=5, b=5))

# Call the function supplying both parameters/arguments
print(calcarea2(5, 5))

# Call the function omitting the default parameter
print(calcarea2(5))

# Call a function with an arbitrary number of arguments
print(mean(1, 2, 3, 4, 5))

print(func1(a=1, b=2, c=3))


