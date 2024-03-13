#!/usr/bin/env python3

# edited by: Joseph Lemois

 # add y/n statement start loop
 # display a welcome message
print("\nThe Test Scores application\r\n")
more_scores = "y"  #cant use continue as variable

"""
Comment block to remove provided code

 while True:
    #test_score = (input("Enter test score: "))   #removed int to allow for end
    #if test_score == "end":
        #break
    #else:
        #test_score = int(test_score)
        #if test_score >= 0 and test_score <= 100:
            #score_total += test_score
            #counter += 1      
        #else:
            #print(f"Test score must be from 0 through 100. "
                  #f"Score discarded. Try again.")
                  
"""

while more_scores.lower() == "y":
    print("Enter test scores below."
          "\nEnter 'end' to end the input.")
    print("_"*30+"\r\n")

    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0

    # While loop that runs while input is not "end"
    while (test_score := input("Enter test score: ").lower()) != "end":
        test_score = int(test_score)
        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        else:               #typed out from above instead of copy
            print(f"Test score must be from 0 through 100. "
                  f"Score discarded. Try again.")


    # calculate average score
    average_score = round(score_total / counter)
                    
    # format and display the result
    # add more scores input 
    print("="*30)
    print(f"Total scores entered:\t{counter}"
          f"\nOverall total Score:\t{score_total}"
          f"\nOverall average Score:\t{average_score}")
    more_scores = input("\nEnter another set of test scores (y/n): ")
    print()
print("Good-bye!")


