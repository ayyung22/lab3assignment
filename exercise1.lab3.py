# --------------------------------------------------------
# Lab 1: Getting Started with Python
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 9/21/24

## Exercise 1: While Loop

print("Exercise 1: While Loop")
num = 1
while num <= 10:
    if num == 7:
        break
    print(num)
    num += 1

print()
print()

# Exercise 2: For Loop

print("Exercise 2: For Loop")
my_string = "CIS103Lab3"
for index, char in enumerate(my_string):
    print(f"Index: {index}, Character: {char}")

print()
print()

# Exercise 3: Nested Loop

print("Exercise 3: Nested Loop")
for i in range(1,6):
    for j in range(i):
        print('*', end='')
    print()

print()
print()

# Exercise 4: Break and Continue

print("Exercise 4: Break and Continue")
num = 1
while num <= 10:
    if num == 7:
        break
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1

print()
print()