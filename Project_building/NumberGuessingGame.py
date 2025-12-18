import random

secret = random.randint(1, 100)
attempts = 0

print("Welcome to Smart Guessing Game!")

while True:
    guess = int(input("Guess the number (1–100): "))
    attempts += 1

    if guess == secret:
        print("Correct! You won in", attempts, "attempts")
        break
    elif abs(secret - guess) <= 5:
        print(" Very close!")
    elif abs(secret - guess) <= 10:
        print(" Close")
    else:
        print(" Far away")

    if attempts == 7:
        print(" Too many attempts. The number was:", secret)
        break
