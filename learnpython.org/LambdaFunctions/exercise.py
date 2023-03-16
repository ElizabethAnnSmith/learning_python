# Tutorial exercise

# Write a program using lambda functions to check if a number in the given list is odd.
# Print 'True' is the number is odd or 'False' if not for each element.

l = [2,4,7,3,14,19]
for i in l:
    lamba_function = lambda x : (x % 2) == 1
    print(lamba_function(i))
