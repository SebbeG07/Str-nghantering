import random

randomnumber = random.randint(1, 100)
max_tries = 7
tries = 0

print("Guess the right number between 1-100!")

while tries < max_tries:
    try:
        guess = int(input(f"Tries {tries + 1}: Guess a number: "))
        
        if guess > randomnumber:
            print("Too High!")
        elif guess < randomnumber:
            print("Too Low!")
        else:
            print("Good job! You guessed correct!")
            break  # Exit the loop if the guess is correct
        
        tries += 1  # Increment tries only after a valid input
    except ValueError:
        print("Invalid input! Please enter a number.")

if tries == max_tries and guess != randomnumber:
    print(f"Sorry, you've guessed wrong 7 times. The correct number was {randomnumber}.")
