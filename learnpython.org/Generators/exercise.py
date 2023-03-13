# Tutorial exercise

# Write a generator function which returns the Fibonacci series
# The first two numbers of the series are always equal to 1
# Each consecutive number is the sum of the last two numbers
# Hint: Can you use only two variables in the generator function? Remember that assignments can be done simultaneously

# fill in this function
def fib():
    pass #this is a null statement which does nothing when executed, useful as a placeholder.

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
