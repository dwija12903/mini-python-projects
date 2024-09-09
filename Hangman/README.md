# 🎮 Hangman Game

This is a simple **Hangman Game** developed in Python. The game randomly selects a word, and the player has to guess it one letter at a time. The player has a limited number of incorrect guesses before they lose the game.

## 🌟 Features

- Randomly selects a word from a predefined list.
- Provides visual feedback of remaining lives with a simple hangman graphic.
- Tracks used letters and provides live feedback on the current word.
- Allows players to make guesses until they either win or lose (run out of lives).

## 🚀 How to Run the Game

1. Clone the repository:
   ```bash
   git clone https://github.com/dwija12903/hangman-game.git
   cd hangman-game
   ```

2. Install necessary dependencies (if any).

3. Make sure you have the `words.py` and `hangman_visual.py` files in the same directory as `hangman.py`:
   - `words.py` contains a list of valid words for the game.
   - `hangman_visual.py` contains the visual representation of the hangman as lives decrease.

4. Run the `hangman.py` file:
   ```bash
   python hangman.py
   ```

## 📂 Project Structure

- `hangman.py`: The main Python script that runs the game.
- `words.py`: Contains the list of words used in the game.
- `hangman_visual.py`: Contains the dictionary for the hangman visual as lives decrease.

## 🛠️ How the Game Works

1. The game randomly selects a word from `words.py`.
2. The player guesses a letter at a time.
3. The game updates the current word display, showing correctly guessed letters and dashes for unguessed letters.
4. Each incorrect guess results in the loss of a life, with a visual hangman drawing.
5. The game ends when the player either guesses the word or runs out of lives.

## 🎮 Example

```
You have 6 lives left and you have used these letters: A C E
Current word: _ _ R _ _
Guess a letter: O
```

## 🎉 Winning Condition

If the player guesses all the letters in the word before losing all their lives, they win the game.

## 💀 Losing Condition

If the player runs out of lives, the game is over, and the correct word is revealed.

---

**Enjoy playing!** 🎉