import random
import pathlib
from rich import print
from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

def chooseWord():
    wordlist = pathlib.Path(__file__).parent / 'words.txt'
    words = [
        word.upper()
        for word in wordlist.read_text("utf-8").split("\n")
    ]
    return random.choice(words)

def showGuesses(guesses, word):
    for guess in guesses:
        styledGuess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = 'bold white on green'
            elif letter in word:
                style = 'bold white on yellow'
            else:
                style = 'dim'
            styledGuess.append(f'[{style}]{letter}[/]')
        console.print(''.join(styledGuess), justify='center')

def refresh_page(headline):
    console.clear()
    console.rule(headline)

def guessWord(turn, correct):

    print(f'Turn number {turn}')
    guesses = ['_' * 5] * 6

    for i in range(6):
        refresh_page(headline=f"Guess {i + 1}")
        showGuesses(guesses, correct)
        guess = input('\nEnter your guess: ').upper()
        while len(guess) != 5:
            guess = input('Please enter a 5-letter word: ').upper()
        guesses[i] = guess
        if guesses[i] == correct:
            break

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