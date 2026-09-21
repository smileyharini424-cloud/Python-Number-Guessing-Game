# Python Number Guessing Game

## Explanation

This project is a simple number guessing game developed using Python. The computer generates a random number between 1 and 10, and the user tries to guess it.

## Problem Statement

Create a Python program that generates a random number and allows the user to guess the number until the correct number is entered.

## Features

* Generates a random number.
* Accepts user guesses.
* Indicates whether the guess is too high or too low.
* Counts the number of attempts.
* Displays a success message when the correct number is guessed.

## How It Works

1. The program generates a random number between 1 and 10.
2. The user enters a guess.
3. The program compares the guess with the generated number.
4. It displays whether the guess is too high or too low.
5. The process continues until the correct number is entered.
6. The total number of attempts is displayed.

## Technologies Used

* Python
* `random` module

## Data Structure Used

* No special data structure is required.

## Methods Used

* `random.randint()`
* `input()`
* `while` loop
* Conditional statements

## Program Flow

1. Start the program.
2. Generate a random number from 1 to 10.
3. Set the attempt counter to zero.
4. Ask the user to enter a guess.
5. Increase the attempt counter.
6. Compare the guess with the secret number.
7. Display a suitable message.
8. Repeat until the guess is correct.
9. Display the number of attempts.
10. End the program.

## Sample Input

```text
Enter your guess (1-10): 5
Enter your guess (1-10): 8
Enter your guess (1-10): 7
```

## Sample Output

```text
Too low!
Too high!
Congratulations! You guessed the number.
Attempts: 3
```

## Time Complexity

O(n), where n is the number of attempts.

## Space Complexity

O(1)

## Key Learning

* How to generate random numbers.
* How to use a while loop.
* How to use conditional statements.
* How to count attempts.
* How to build a simple interactive Python game.

## File Location

```text
Python-Number-Guessing-Game/number_guessing_game.py
```

## Repository Structure

```text
Python-Number-Guessing-Game/
│
├── number_guessing_game.py
└── README.md
```

## Author

V.Harini
