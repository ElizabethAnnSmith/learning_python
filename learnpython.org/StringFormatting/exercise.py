# Tutorial exercise

# Write a format string which prints out the data in the following syntax - Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)
