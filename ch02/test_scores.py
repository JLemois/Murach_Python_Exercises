#!/usr/bin/env python3

"""
    Coded By: Joseph Lemois
    Made slight changes compared to what was requested in exercise
"""

# display a welcome message
print("The Test Scores program")
print("_"*30)
print("\nEnter 3 test scores")

# get scores from the user
# add save score variables
total_score = 0      # initialize the variable for accumulating scores
score1 = int(input("Enter first test score: "))
total_score += score1
score2 = int(input("Enter second test score: "))
total_score += score2
score3 = int(input("Enter final test score: "))
total_score += score3

# calculate average score
# edit: add calculate total score
average_score = round(total_score / 3)
             
# format and display the result
# edit: add scores entered
print("_"*30)
print(f"\nYour Scores are: \t\t{score1}, {score2}, {score3}"
      f"\nYour total score is: \t{total_score}"
      f"\nYour average score is:\t{average_score}")
print("\n\tGood-bye!")


