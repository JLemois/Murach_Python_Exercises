#!/usr/bin/env python3

# Edit By: Joseph Lemois
import validation as valid  #check spelling of import file
"""
validation file is a get_float and get_int functions that call for prompts
have validation settings for higher and lower boundaries and will
loop for correction or return values if correct
"""

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    return future_value
"""
function get_float will have a prompt section for the statement & input
followed by lower validation then higher validation
number is used for numbers that are input
"""
#def get_float():
    #while True:    # this didnt work moving forward past first request.
        #monthly_investment = float(input("Enter monthly investment:\t"))
        #if monthly_investment <=0 and monthly_investment => 1000
            #return monthly_investment #misunderstood that arguments should have been in function parentheses
        #else:
            #print("Entry must be greater than 0 and less than or equal to 1000.")

#def get_float(prompt, lower, higher):
    #while True:
        #number = float(input(prompt))   # input cannot be variable
        #if number > lower and number <= higher:
            #return number
        #else:
            #print("Entry must be greater than", lower, "and less than or equal to", higher)

#def get_int(prompt, lower, higher):
    #while True:     #mock get_float function
        #numbers = int(input(prompt))
        #if numbers > lower and numbers <= higher:
            #return numbers
        #else:
            #print("Entry must be greater than", lower, "and less than or equal to", higher)
    


def main():
    choice = "y"
    while choice.lower() == "y":
        print("Welcome to the Future Value Calculator")   # add heading and space
        print()
        # get input from the user #add valid. to existing functions for use of import
        #monthly_investment = float(input("Enter monthly investment:\t"))
        #monthly_investment = getfloat()
        monthly_investment = valid.get_float("Enter monthly investment:\t", 0, 1000)
        #yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        yearly_interest_rate = valid.get_float("Enter yearly interest rate:\t", 0, 15)
        #years = int(input("Enter number of years:\t\t"))
        years = valid.get_int("Enter number of years:\t\t", 0, 50)
        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        print()   #add space to match book example
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Goodbye!")   #change to goodbye, softer exit
    
if __name__ == "__main__":
    main()
