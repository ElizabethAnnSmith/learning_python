# Learning to write a function
block_head:
    1st block line
    2nd block line
    ...
# block_line is python code or another block
# block_head is has this format: block_keyword block_name(arguement1, arguement2, ...)
# Examples of block_keywords are 'if', 'for' and 'while'
# Functions are defined using the block_keyword 'def' followed by a name

def my_function():
    print("Hello From My Function!")


# Functions can receive arguments
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


# Using return
def sum_two_numbers(a, b):
    return a + b


# Calling functions in Python
# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
