# Learning boolean conditions
x = 2
print(x == 2) # True
print(x == 3) # False
print(x < 3) # True


# Using boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John and you are 23 years old")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick")


# Using the 'in' operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick")


# Using if statements
statement = False
another_statement = True
if statement is True:
    print("statement is True")
    pass
elif another_statement is True: 
    print("another_statment is True")
    pass
else:
    print("Neither is True")
    pass 


# Another if statement
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal two.")


# Using the 'is' operator
x = [1,2,3]
y = [1,2,3]
print(x == y) # True
print(x is y) # False


# Using the 'not' operator
print(not False) # True
print((not False) == (False)) # False
