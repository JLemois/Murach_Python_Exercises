#!/usr/bin/env python3

# Edit By: Joseph Lemois
import validation as valid

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

def main():
    choice = "y"
    while choice.lower() == "y":
        print("\nWelcome to the Future Value Calculator\r\n")   # add heading and space
        # get input from the user   add valid. to existing functions
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
        print(f"\nYour Future value is:\t\t{round(future_value, 2)}")

        # see if the user wants to continue
        choice = input("\nContinue? (y/n): ")

    print("\nGood-bye!")
    
if __name__ == "__main__":
    main()
