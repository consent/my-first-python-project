# This is a really simple script that will ask for your name
# Then, it'll ask for your age and tell you how old you'll be in 10 years!

print("Hello there!")
print("I hope you're having a great day!")

# Ask for name
name = input("What's your name? ")

# Ask for age
age = input("How old are you? ")

# Make sure the user entered a number for age
try:
    age = int(age)
except ValueError:
    print("Oops! That doesn't seem like a valid number. I'll assume you meant 20.")
    age = 20

# Calculate the age in 10 years
age_in_10_years = age + 10

# Print the result
print("Thanks, " + name + "! You'll be " + str(age_in_10_years) + " years old in 10 years!")
print("Isn't that exciting?")

# Now, let's do something a little more random
print("Let's see if you can guess a number I'm thinking of...")

import random
number_to_guess = random.randint(1, 10)
user_guess = input("Guess a number between 1 and 10: ")

# Check if the guess is correct
if user_guess.isdigit():
    user_guess = int(user_guess)
    if user_guess == number_to_guess:
        print("Wow, you guessed it!")
    else:
        print("Oops, that's not it. The number was " + str(number_to_guess))
else:
    print("That's not a number... Try again!")

# A little thank you note at the end
print("Thanks for playing with my first Python script!")
print("See you next time, " + name + "!")
