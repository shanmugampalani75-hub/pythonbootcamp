import os
import sys
import datetime
import random

#basically this line is used to access a file from different folder
#similar like using cd command in the terminal
#sys.path.append = cd, os.path.dirname = . function in the cd .  
sys.path.append(os.path.dirname(os.path.abspath(__file__))) #Adjust path for imports to root directory

now = datetime.datetime.now()
today = datetime.date.today()
formatted_date = now.strftime("%d-%m-%ys %H:%M:%S")

print(f"Now date: {now}")
print(f"Today's Date: {today}")
print(f"Current Date and Time: {formatted_date}")

random_number = random.randint(1, 100)
random_choice = random.choice(["apple", "banana", "durian"])
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print(f"Random Number: {random_number}")
print(f"Random Choice: {random_choice}")
print(f"Shuffled Numbers: {numbers}")

