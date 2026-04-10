"""
Number Guessing Game: "Higher", "Lower", or "Correct!".
    - Hint: Use random.randint.
    - Components: random, attempts.

"""

import random

secret = random.randint(1, 100)
attempt = 0

print("I'm thinking of a number between 1 and 100.")


while True:
    try:
        guess = int(input("Enter your guess: "))
    
        if guess > secret:
            print("Too high!")
            attempt += 1
        elif guess < secret:
            print("Too low!")
            attempt += 1
        else:
            print(f"Correct! You got it in {attempt} tries")
            break
    except ValueError as e:
        print(e)
