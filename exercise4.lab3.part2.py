# -------------------------------------------------------- #
# Lab 3: Python Loops and Object Types
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 9/21/2024

import statistics
#defining mean, median, and mode

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 +mid2) / 2
    else:
        return sorted_numbers[n // 2]

def mode(numbers):
    frequency = { }
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    mode_data = max(frequency, key=frequency.get)
    return mode_data

#example of a number list and will print the mode, median, and mean
numbers = [6, 6, 7, 8, 9, 10, 12, 9, 9, 9, 22]
print("The mode is:", mode(numbers))
print("The median is:", median(numbers))
print("The mean is:", mean(numbers))

