# Hangman Game

Welcome to the Hangman game! This is a simple Python implementation of the classic word-guessing game that allows you to input any word or phrase you want to play with.

## Features

- Play with any word or phrase.
- Visual representation of the hangman for each incorrect guess.
- Keeps track of the guessed letters.
- Allows for a maximum of 6 incorrect attempts.

## How to Run the Game

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Execute

1. **Clone or Download the Repository**: Download the Hangman game code to your local machine.

2. **Create a Python File**:
   - Open a text editor (like Notepad, Visual Studio Code, or any IDE you prefer).
   - Copy the Hangman game code and paste it into the editor.
   - Save the file as `hangman.py`.

3. **Open Terminal**:
   - Open the terminal (Command Prompt on Windows, Terminal on macOS or Linux).

4. **Navigate to the Directory**:
   - Use the `cd` command to navigate to the directory where you saved the `hangman.py` file. For example:
     ```bash
     cd path/to/your/directory
     ```

5. **Run the Python File**:
   - In the terminal, type the following command and hit Enter:
     ```bash
     python hangman.py
     ```
   - If you're using Python 3 and the command above doesn’t work, try:
     ```bash
     python3 hangman.py
     ```

6. **Input Word or Phrase**:
   - When prompted, enter a word or phrase you want to use for the Hangman game. Spaces will be replaced with underscores for the game display.

7. **Guess Letters**:
   - Enter one letter at a time to guess the word or phrase. The game will track your guesses and display the current state of the word or phrase, along with the hangman graphic.

## Game Rules

- You have 6 attempts to guess the word or phrase correctly.
- If you guess a letter that is not in the word or phrase, you lose an attempt.
- The game ends when you either guess the word or phrase completely or run out of attempts.
