#!/usr/bin/env python3

# display a welcome message
print("\nThe Test Scores application\r\n"
      "\nEnter the test scores below"
      "\nEnter 'x' to quit the program\r\n")
print("="*30)

# initialize variables
counter = 0
score_total = 0
test_score = 0

# while loop tests user input to exit and/or validates int inputs within range
while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score != "x":
        test_score = int(test_score)
        counter += 1
    else:
        break
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.\r\n")

# calculate average score
average_score = round(score_total / counter)
                
# format and display the result
print("="*30)
print(f"\nTotal Score:\t\t\t{score_total}"
      f"\nTotal scores entered:\t{counter}"
      f"\nAverage Score:\t\t\t{average_score}\r\n"
      "\nGood-bye")