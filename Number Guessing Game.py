import math
import random

# Take Inputs

lower = int(input("Lower bound:- "))

upper = int(input("Upper bound:- "))
 
# generating random number between the lower and upper

x = random.randint(lower, upper)

print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
 
# Number of guesses
count = 0
 
while count < math.log(upper - lower + 1, 2):
    count += 1
 
# Guessing number input
guess = int(input("Guess a number:- "))
 
# Condition testing
if x == guess:
    print("Congratulations you did it in ",
            count, " try/tries")
    break
elif x > guess:
    print("You guessed too small!")
elif x < guess:
    print("You Guessed too high!")
 
# more than required guesses
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
 

