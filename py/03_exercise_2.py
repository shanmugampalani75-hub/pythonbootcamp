##Create a simple quiz program with 3 questions.

score = 0

##Question 1
answer1 = input("What is the capital of France?").lower()
if answer1 == "paris":
    print("Correct")
    score += 1
    print(score)
else:
    print("Wrong! The answer is Paris.")

##Question 2
answer2 = input ("What is the largest planet in our solar system?").lower()
if answer2 == "jupiter":
    print("Correct")
    score += 1
    print(score)
else:
    print("Wrong! The answer is Jupiter.")

##Question 3
answer3 = input("What is the chemical symbol for gold?").lower()
if answer3 == "au":
    print("Correct")
    score += 1
    print(score)
else:
    print("Wrong! The answer is Au.")


##Final Score

print(f"Your final score is {score}/3.")
if score == 3:
    print("Perfect score!")
elif score == 2:
    print("Good job!")
elif score == 1:
    print("Better luck next time!")
else:
    print("Keep trying!")