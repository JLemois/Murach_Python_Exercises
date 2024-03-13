#!/usr/bin/env python3

"""
    Coded By: Joseph Lemois
    Made slight changes compared to what was requested in exercise
"""

# display a welcome message
print("\nThe Miles Per Gallon program")
print("_"*30)

# get input from the user
# edit: add cost of gas
miles_driven= float(input("Enter miles driven:\t\t\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t\t"))
cost_of_gas = float(input("Enter cost of a gallon of gas:\t"))

# calculate miles per gallon
# edit: add formula for total gas cost & cost per mile
# mpg is miles per gallon
# tgc is total gas cost
# cpm is cost per mile
mpg = round(miles_driven / gallons_used, 1)
tgc = round(gallons_used * cost_of_gas, 2)
cpm = round(tgc / miles_driven, 2)
            
# format and display the result
# edit: add results for total cost and cost per mile
print(f"\nMiles Per Gallon:\t\t{mpg}"
      f"\nTotal Gas Cost:\t\t\t${tgc}"
      f"\nCost Per Mile:\t\t\t${cpm}"
      "\n\n\tGood-bye!")