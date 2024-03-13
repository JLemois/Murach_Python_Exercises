#!/usr/bin/env python3

# Edit By: Joseph Lemois
        
"""
function get_float will have a prompt section for the statement & input
followed by lower validation then higher validation
number is used for numbers that are input
"""
"""
def get_float():
    while True:    
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment <=0 and monthly_investment => 1000
            return monthly_investment #misunderstood that arguments should have been in function parentheses
        else:
            print("Entry must be greater than 0 and less than or equal to 1000.")
"""
def get_float(prompt, lower, higher):
    while True:
        number = float(input(prompt))
        if number > lower and number <= higher:
            return number
        else:
            print("Entry must be greater than ", lower, ", and less than or equal to ", higher)

def get_int(prompt, lower, higher):
    while True:     #mock get_float function
        numbers = int(input(prompt))
        if numbers > lower and numbers <= higher:
            return numbers
        else:
            print("Entry must be greater than ", lower, ", and less than or equal to ", higher)

def main():
    choice = "y"
    while choice.lower() == "y":

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
