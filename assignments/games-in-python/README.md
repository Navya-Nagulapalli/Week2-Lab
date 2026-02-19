
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game to practice string manipulation, control flow, and user input handling in Python. The player will guess letters to uncover a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Implement Hangman Game

#### Description
Create a playable Hangman game that runs in the terminal. The program should manage the game loop, accept user input for guesses, display progress, and determine win/lose outcomes.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Prompt the player for single-letter guesses (case-insensitive)
- Display the current word progress using underscores for unknown letters (e.g. `_ a _ _ m a n`)
- Track and display letters already guessed and remaining incorrect attempts
- Ignore repeated guesses without penalizing the player
- End the game when the word is fully guessed or attempts are exhausted, showing a win or lose message
- Provide a clear, user-friendly command-line interface

#### Example

Starting round:

```
Welcome to Hangman!
Word: _ _ _ _ _
Guesses remaining: 6
Guessed letters: 
Enter a letter: a
```

### 🛠️ Optional Enhancements

#### Description
Add one or more enhancements to improve gameplay, usability, or replayability.

#### Requirements

- Add difficulty levels that change the number of allowed incorrect guesses
- Display ASCII-art hangman progress for incorrect guesses
- Provide a hint system or word categories
- Allow the player to play multiple rounds without restarting the program

---

**Skills practiced:** String manipulation, loops, conditionals, randomness, basic UX for CLI

Place your solution in `starter-code.py` and keep helper functions modular for testing.
