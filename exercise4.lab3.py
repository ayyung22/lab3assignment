# -------------------------------------------------------- #
# Lab 3: Python Loops and Object Types
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 9/21/2024

import math

# Get the radius from the user
r = float(input("Please enter the radius of the sphere: "))

# Calculate diameter, circumference, surface area, and volume
diameter = 2 * r
circumference = 2 * math.pi * r
surface_area = 4 * math.pi * r**2
volume = (4/3) * math.pi * r**3

# Print the results
print("Diameter:", diameter)
print("Circumference:", circumference)
print("Surface Area:", surface_area)
print("Volume:", volume)
