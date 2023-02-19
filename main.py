#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
print(logo)
import random
print("Welcome to the number guessing game!")
print("I'm thinking of a number betwwn 1 and 100")
correct_answer=random.randint(1,100)
print(f"the correct answer is {correct_answer}")
diff_level=input("choose a difficulty.Type 'easy' or 'hard': ")
if diff_level=="hard":
  attempts=5
else:
  attempts=10
for i in range(attempts,0,-1):
  print(f"You have {i} attempts remaining to guess a number")
  guess_num=int(input("Make a guess: "))
  if guess_num==correct_answer:
    print(f"you got it.The answer was {guess_num}")
    break 
  elif guess_num<correct_answer:
    print("Too low")
    if i==1:
      print("you've ran out of guesses, you loose")
    else:
      print("Guess again")
  else:
    print("Too high")
    if i==1:
      print("you've ran out of guesses, you loose")
    else:
      print("Guess again")
