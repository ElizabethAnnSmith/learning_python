# Tutorial exercise

# Create a string, integer and floating point number. 
# String should be named mystring and should contain the word 'hello'.
# Floating point number should be named myfloat and contain number 10.0.
# Integer should be named myint and contain number 20.

mystring = "hello"
myfloat = 10.0
myint = 20

# Test code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
