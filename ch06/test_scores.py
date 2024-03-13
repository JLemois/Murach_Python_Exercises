#!/usr/bin/env python3

#Lemois Joseph, CPT-168-S47, Lab06-1, Test_Scores

# welcome message and guidance through program for user
def display_welcome():
    print("\nThe Test Scores program\r\n"
          "\nEnter 'x' to quit\r\n")
    print("_"*30+"\r\n")

# gets and validates scores
def get_scores():
    score_total = 0
    counter = 0
    while True:
        score = input("Enter test score: ")
        if score == "x":
            print("_"*30)
            return  score_total, counter
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                score_total += score
                counter += 1 
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(score_total, count):
    # calculate average score
    average = score_total / count
                
    # format and display the result
    print(f'\nScore total:\t\t{score_total}'
          f'\nNumber of Scores:\t{count}'
          f'\nAverage Score:\t\t{average}')
def main():
    display_welcome()
    score_total, count = get_scores()
    process_scores(score_total, count)
    print("\nGood-bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


