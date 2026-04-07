Number Guessing Game (Refactored)
A simple console-based number guessing game built with Python. This project demonstrates how to refactor procedural code into modular functions using parameters and return values.
🎯 Features
Difficulty Levels: Choose between Easy (1-10), Medium (1-50), and Hard (1-100).
Attempt Tracking: The game keeps track of how many guesses it takes to find the correct number.
Input Validation: Includes a basic try/except block to prevent crashes if a user enters a non-integer.
Clean Structure: Organized into logical functions for better readability and reusability.
🛠️ How to Run
Make sure you have Python installed.
Download or clone this repository to your local machine.
Open your terminal or command prompt.
Navigate to the project folder and run:
bash
python your_filename.py
Use code with caution.

🧠 Code Structure
The code was refactored from a single script into three main parts:
set_difficulty(): Handles user input for the level and returns the maximum number range.
play_game(secret_number, max_limit): The core engine. It takes the target number and range as parameters and runs the guessing loop.
main(): The "driver" function that connects everything together.
if __name__ == "__main__":: A safety switch that ensures the game only runs when you execute the file directly, allowing it to be safely imported into other scripts.
📝 Example Output
text
Choose a level: 1 (Easy 1-10), 2 (Medium 1-50), 3 (Hard 1-100)
Enter 1, 2 or 3: 1

Welcome! I'm thinking of a number between 1 and 10
Guess a number (1-10): 5
Too high!
Guess a number (1-10): 3
Great job! You got it in 2 attempts.
