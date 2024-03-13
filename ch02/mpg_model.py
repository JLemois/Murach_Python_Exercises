#!/usr/bin/env python3

# display a welcome message
print("\nThe Miles Per Gallon program")
print("_"*30)
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))

# calculate miles per gallon
mpg = round((miles_driven / gallons_used), 1)

# format and display the result
print()
print(f"Miles Per Gallon:\t\t\t{mpg}")
print()
print("Good-bye!")