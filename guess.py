
print("Hello. What's your name?")
name = raw_input()

import random
prizenum = random.randrange(1,101)
print prizenum

print "Hi %s, I have a number between 1 and 100 for you to guess, what is your guess?" % name

# Our first attempt at the guessing game, less efficient code, commented out upon update
# while guess != prizenum:
#     # numtries = 2
#     guess = int(raw_input()) 
#     if guess > prizenum:
#         print "Your guess is too high. Guess again"
#     elif guess < prizenum:
#         print "Your guess is too low. Guess again"
#     numtries += 1

#Commented out working code for guessing game, now going to try as a function
# numtries = 0

# while True:
#     guess = int(raw_input())
#     numtries += 1
#     if guess > prizenum:
#         print "Your guess is too high. Guess again"
#     elif guess < prizenum:
#         print "Your guess is too low. Guess again"
#     else:
#         print "Congrats %s! You guessed our number in %d tries!" % (name, numtries)
#         break
    
def game():
    numtries = 0
    while True:
        try:
            guess = int(float(raw_input()))
            numtries += 1
            if guess > 100 or guess < 1:
                print "We said BETWEEN 1-100! Try guessing again."
            else:
                if guess > prizenum:
                    print "Your guess is too high. Guess again"
                elif guess < prizenum:
                    print "Your guess is too low. Guess again"
                else:
                    print "Congrats %s! You guessed our number in %d tries!" % (name, numtries)
                    break
        except ValueError:
            print("Sorry. You must enter a number as a guess. Please guess again.")

game()
