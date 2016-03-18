# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for s in secretWord:
        if s not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter
        else:
            word += '_'
    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string

    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter in lettersGuessed:
            alphabet = alphabet.replace(letter,"")
    return alphabet

def victory(secretWord, lettersGuessed):
    print("-------------")
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was {}".format(secretWord))


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessLeft = 8
    lettersGuessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))

    while guessLeft > 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        print("-------------")
        print("You have {} guesses left.".format(guessLeft))
        print("Available letters: {}".format(getAvailableLetters(lettersGuessed)))

        guess = raw_input("Please guess a letter: ").lower()

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        elif guess not in secretWord:
            lettersGuessed.append(guess)
            print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            guessLeft -= 1
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        else:
            break
    victory(secretWord, lettersGuessed)

def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
    else:
        print "1"
    finally:
        print "0"

FancyDivide([0, 2, 4], 1)
