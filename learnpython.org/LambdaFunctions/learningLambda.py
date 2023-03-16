# Learning about Lambda functions

# instead of using this ...
def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)

# We can use something like: function_name = lambda inputs : outputs

a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)
