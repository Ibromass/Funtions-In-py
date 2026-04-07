import random

# This function just helps us pick the difficulty level
def set_difficulty():
    print("Choose a level: 1 (Easy 1-10), 2 (Medium 1-50), 3 (Hard 1-100)")
    level = input("Enter 1, 2 or 3: ")
    
    # Check what the user typed and return the max number
    if level == '1':
        return 10
    elif level == '2':
        return 50
    elif level == '3':
        return 100
    else:
        # If they type something weird, just give them Easy mode
        print("Invalid input, defaulting to Easy.")
        return 10

# This is the actual game loop logic
# We pass in the secret number and the max limit as parameters
def play_game(secret_number, max_limit):
    attempts = 0
    while True:
        # Get the guess from the user
        guess = int(input(f"Guess a number (1-{max_limit}): "))
        attempts += 1 # Add 1 to the try counter
        
        # Compare the guess to our secret number
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high!")
        else:
            # If they get it right, show the attempts and stop the loop
            print(f"Great job! You got it in {attempts} attempts.")
            break 

# This is where the program actually starts
def main():
    # First, get the max number from our setup function
    max_num = set_difficulty()
    
    # Use that number to make our random secret number
    random_number = random.randint(1, max_num)
    
    print(f"Welcome! I'm thinking of a number between 1 and {max_num}")
    
    # Now start the game by passing our variables into the function
    play_game(random_number, max_num)

# This part makes sure the game only starts if we run this file directly
if __name__ == "__main__":
    main()

