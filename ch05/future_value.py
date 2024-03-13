#!/usr/bin/env python3

# Joseph Lemois Feb. 11 2022, cpt-168-S47,Lab05-2

# get float function that validates user input
def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")

# Get int function that validates user input
def get_integer(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")
            
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(1, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    print("\nFuture Value calculator")
    print("_"*30)
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float("\nEnter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_float("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print(f"\nYour Future value is:\t\t${round(future_value, 2)}\r\n")

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")

    print("\nBye!")
    
if __name__ == "__main__":
    main()
