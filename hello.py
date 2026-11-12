#!/usr/bin/env python

# x = 1
# y = 2
# import ipdb

# ipdb.set_trace()
# print(x + y)


# Create a hello function that uses f-strings
def hello(name):
    print(f"Hello, {name}!")


# call the function using if __name__ == "__main__"
if __name__ == "__main__":
    hello("World")
    hello("Python")

# Create a list with different types of fruit
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# loop through the fruits and count the total fruits in the list
for fruit in fruits:
    # use an f-string to print the fruit name and the number of the fruit in the list
    print(f"{fruits.index(fruit) + 1}. {fruit}")

# the total number of fruits in the list
print(f"Total fruits: {len(fruits)}")
