# Print the number of characters including punctuation and spaces
astring = "Hello world!"
print(astring.index("o")) # This prints out 4 because the first 'o' is 4 characters away from first character
print(astring.count("l")) # Prints out the number of l's 
print(astring[3:7]) # Prints a slice of string, starting a 3 and ending at 6
print(astring[2]) # Prints single character
print(astring[:6]) # Slice starting at beginning to given number
print(astring[-1:-3]) # Negative number starts at end of string
print(astring[3:7:2]) # Prints characters 3-7 skipping one character [start:stop:step]

# These two print the same thing
print(astring[3:7])
print(astring[3:7:1])

print(astring[::-1]) # Reverse string
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ") # Split the string into a list of seperate strings
print(afewwords)
