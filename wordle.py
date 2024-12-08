import random
import pathlib
from rich import print
from rich.console import Console
from rich.theme import Theme
from string import ascii_letters
from string import ascii_uppercase

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

def chooseWord():
    wordlist = pathlib.Path(__file__).parent / 'words.txt'
    words = [
        word.upper()
        for word in wordlist.read_text("utf-8").split("\n")
    ]
    return random.choice(words)

def showGuesses(guesses, word):
    letter_status = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        styledGuess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = 'bold white on green'
            elif letter in word:
                style = 'bold white on yellow'
            elif letter in ascii_letters:
                style = 'bold white on #666666'
            else:
                style = 'dim'
            styledGuess.append(f'[{style}]{letter}[/]')
            if letter != "_":
                letter_status[letter] = f"[{style}]{letter}[/]"
        console.print(''.join(styledGuess), justify='center')
    console.print("\n" + "".join(letter_status.values()), justify="center")

def refresh_page(headline):
    console.clear()
    console.rule(headline)

def guessWord(turn, correct):

    print(f'Turn number {turn}')
    guesses = ['_' * 5] * 6

    refresh_page(headline=f"Guess {0 + 1}")
    showGuesses(guesses, correct)

    for i in range(6):
        guess = input('\nEnter your guess: ').upper()
        while len(guess) != 5:
            guess = input('Please enter a 5-letter word: ').upper()
        guesses[i] = guess
        if guesses[i] == correct:
            refresh_page(headline=f"Guess {i + 1}")
            showGuesses(guesses, correct)
            break
        refresh_page(headline=f"Guess {i + 1}")
        showGuesses(guesses, correct)

    result(correct, guesses)


def result(correct, guesses):
    if correct in guesses:
        print('[bold green]You guessed the word!')
    else:
        print(f'[bold red]The correct word is {correct}')

def main():
    correct = chooseWord()
    turn = 1
    guessWord(turn, correct)

main()