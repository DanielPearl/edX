from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList) == True:
            # Find out how much making that word is worth
            current_score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if current_score > max_score:
                # Update your best score, and best word accordingly
                max_score = current_score
                best_word = word

    # return the best word you found.
    return best_word

compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, WORDLIST_FILENAME, 5)
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)

    # Keep track of the total score
    total_score = 0
    copied_hand = hand.copy()
    # As long as there are still letters left in the hand:
    while calculateHandlen(copied_hand) > 0:
        # The computer chooses a word
        print "Current Hand:", displayHand(copied_hand)
        # Ask user for input
        word = compChooseWord(copied_hand, wordList, n)

        if word != None:
            score = getWordScore(word, n) # Score for each word
            total_score += score # Increment total score for all words
            print('"{0}" earned {1} points. Total: {2} points'.format(word, score, total_score)) # Print word score

            copied_hand = updateHand(copied_hand, word)
        else:
            break

    print("Total score: {}".format(total_score))


compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, WORDLIST_FILENAME, 5)

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    user, hand = None, {}
    copied_hand = hand.copy()

    while user != 'e':
        user = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        if user == 'e':
            break
        elif user == 'n':
            copied_hand = dealHand(HAND_SIZE)
            print

            while user != 'u' or user != 'c' :
                user = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if user == 'u':
                    print
                    playHand(copied_hand, wordList, HAND_SIZE)
                    print
                    break
                elif user == 'c':
                    print
                    compPlayHand(copied_hand,wordList,HAND_SIZE)
                    print
                    break
                else:
                    print("Invalid command\n")

        elif user =='r':
            if copied_hand != {}:
                while user != 'u' or user != 'c':
                    user = raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if user == 'u':
                        print
                        playHand(copied_hand, wordList, HAND_SIZE)
                        print
                        break
                    elif user == 'c':
                        print
                        compPlayHand(copied_hand,wordList,HAND_SIZE)
                        print
                        break
                    else:
                        print("Invalid command\n")
            else:
                print("You have not played a hand yet. Please play a new hand first!")
        else:
            print("Invalid command.\n")



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
