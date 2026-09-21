import random
secret_number = random.randint(1, 10)
attempts = 0
while True:
    guess = int(input("Enter your guess (1-10): "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Congratulations! You guessed the number.")
        print("Attempts:", attempts)
        break
