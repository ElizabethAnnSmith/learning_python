# A basic class
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

# To access 'variable' we need to use
# myobjectx.variable
# for example
print(myobjectx.variable)

# Can add a second object
myobjectY = MyClass()
myobjectY.variable = "yackity"
print(myobjectY.variable)

