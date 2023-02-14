# Learn to build a list
myList = []
myList.append(1)
myList.append(2)
myList.append(3)
print(myList[0]) # prints 1
print(myList[1]) # prints 2
print(myList[2]) # prints 3

# Prints all
for x in myList:
    print(x)


# Accessing an index that doesn't exist generates an exception
myList = [1,2,3]
print(myList[10])
