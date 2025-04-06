def display_hangman(attempts):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |
           |
        ''',
        '''
           ------
           |    |
           |    O
           |
           |
           |
        ''',
        '''
           ------
           |    |
           |
           |
           |
           |
        ''',
    ]
    # Ensure attempts do not exceed the list's index
    return stages[min(attempts, len(stages) - 1)]

def hangman():
    word = input("Enter a word or phrase for the Hangman game: ").lower()
    word = word.replace(' ', '_')  # Replace spaces with underscores for display
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    
    while attempts > 0 and '_' in guessed:
        print(display_hangman(attempts))
        print("Word:", ' '.join(guessed))
        print("Guessed Letters:", ' '.join(guessed_letters))
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed[index] = guess
        else:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts left.")
        
    if '_' not in guessed:
        print("Congratulations! You've guessed the word:", word.replace('_', ' '))
    else:
        print(display_hangman(attempts))
        print("Sorry, you've run out of attempts. The word was:", word.replace('_', ' '))

if __name__ == "__main__":
    hangman()
