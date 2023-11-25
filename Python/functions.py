#Defining a function
"""
def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(3, 4)
print(out)

"""
"""
def summ(arg):
    x = 0
    for i in arg:
        x += i
    return x

print(sum([1,5,4,6,3,2,5,2,5,3]))
"""
#Default Argument
"""
def greetings(MSG="Morning"):
    print(f"Good {MSG}!")
    print("Welcome to the function.")

greetings("Evening")
"""