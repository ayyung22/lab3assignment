# -------------------------------------------------------- #
# Lab 3: Python Loops and Object Types
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 9/21/2024

#creating a tuple

my_tuple = (4, 5, 6, 7, 8)
print(my_tuple)

#accessing first element of a tuple
print(my_tuple[0])

#accessing last element of a tuple
print(my_tuple[4])

#attempting to change the second element of the tuple
my_tuple[1] = 100
print(my_tuple)

#error when attempting to change the 2nd element of the tuple

#Dictionary operations
my_dictionary = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}

print(my_dictionary)

#adding a new key-value pair for Alice's GPA
my_dictionary["GPA"] = 4.0
print(my_dictionary)

#modifying Alice's name to 23
my_dictionary.update({"age": 23})
print(my_dictionary)

#removing the "major" key from the dictionary
del my_dictionary["major"]
print(my_dictionary)