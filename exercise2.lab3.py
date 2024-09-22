# -------------------------------------------------------- #
# Lab 3: Python Loops and Object Types
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 9/21/2024

#string reversal
def reverse_string(s):
    return s[::-1]

my_string = "Lab3Python"
print(reverse_string(my_string))

print()
print()


#creating a list

my_integers = [1, 2, 3, 4, 5]
print(my_integers)

#adding 6 to the list
my_integers.append(6)
print(my_integers)

#removing the 3rd element from the list
del my_integers[2]
print(my_integers)

#sorting the list in descending order
my_integers.sort(reverse = True)
print(my_integers)



