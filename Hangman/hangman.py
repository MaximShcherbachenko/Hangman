# Problem Set 2, hangman.py
# Name: Maxim Shcherbachenko
# Collaborators: -
# Time spent: 4 - 5 hours

# Hangman Game

import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)



wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    a = ""
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            a += secret_word[i]
        else:
            a += "_ "
    if a == secret_word:
        return True
    return False
#secret_word_test = input("SW:")
def get_guessed_word(secret_word, letters_guessed):
    a = ""
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            a += secret_word[i]
        else:
            a += "_ "
    return a

def get_available_letters(letters_guessed):
    s = string.ascii_lowercase
    for i in range(len(s)):
        if s[i] in letters_guessed:
            s = s.replace(s[i], " ")
    return s
def hangman(secret_word):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    guesses_ramainings = 6
    warnings_remainings = 3
    a = []
    temp = "_ " * len(secret_word)
    while guesses_ramainings > 0:
        print("You have", warnings_remainings, "warnings left.")
        print("You have", guesses_ramainings, "guesses left.")
        print("Available letters:", get_available_letters(a))
        letters_guessed = input("Please guess a letter:\n").lower()
        a.append(letters_guessed)
        if warnings_remainings > 0:
            if not letters_guessed.isalpha() or len(letters_guessed) > 1:
                print("Oops! That is not a valid letter. You have", warnings_remainings - 1,"warnings left:")
                warnings_remainings -= 1
                continue
            if a.count(letters_guessed) > 1:
                print("Sorry, you have already entered this letter.")
                warnings_remainings -= 1
                continue
        if temp == get_guessed_word(secret_word, a) and (letters_guessed == "a" or letters_guessed == "e" or letters_guessed == "i" or letters_guessed == "o" or letters_guessed == "u"):
            guesses_ramainings -= 2
        elif temp == get_guessed_word(secret_word, a):
            guesses_ramainings -= 1
        if get_guessed_word(secret_word, a) != temp:
            print("Good guess:", get_guessed_word(secret_word, a))
            temp = get_guessed_word(secret_word, a)
            print("-" * 26)
        else:
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, a))
            temp = get_guessed_word(secret_word, a)
            print("-" * 26)
        if is_word_guessed(secret_word, a) == True:
            print("Congratulations, you won! Your total score for this game is:", guesses_ramainings*len(set(secret_word)))
            break
        elif guesses_ramainings == 0:
            print("You lose:(\n Secret word:", secret_word)
        else:
            continue
        print()

def match_with_gaps(my_word, other_word):
    if my_word == "_" * len(my_word) or my_word.count("_") == 1 or len(my_word) != len(other_word):
        return False
    for i in range(len(other_word)):
        if my_word[i] == "_":
            continue
        if my_word[i] != other_word[i]:
            return False
    return True
def show_possible_matches(my_word):
    a = ""
    for words in wordlist:
        if match_with_gaps(my_word, words) == True:
            a += words + " "
        else:
            continue
    return a

def hangman_with_hints(secret_word):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    guesses_ramainings = 6
    warnings_remainings = 3
    a = []
    temp = "_ " * len(secret_word)
    while guesses_ramainings > 0:
        print("You have", warnings_remainings, "warnings left.")
        print("You have", guesses_ramainings, "guesses left.")
        print("Available letters:", get_available_letters(a))
        letters_guessed = input("Please guess a letter:\n").lower()
        a.append(letters_guessed)
        print(temp)
        if letters_guessed == "*" and temp.replace(" ", "") != len(secret_word)*"_":
            print(show_possible_matches(temp.replace(" ", "")))
            continue
        elif letters_guessed == "*":
            print("You cant use hints for now.")
            warnings_remainings -= 1
            continue
        if warnings_remainings > 0:
            if not letters_guessed.isalpha() or len(letters_guessed) > 1:
                print("Oops! That is not a valid letter. You have", warnings_remainings - 1, "warnings left:")
                warnings_remainings -= 1
                continue
            if a.count(letters_guessed) > 1:
                print("Sorry, you have already entered this letter.")
                warnings_remainings -= 1
                continue
        if temp == get_guessed_word(secret_word, a) and (
                letters_guessed == "a" or letters_guessed == "e" or letters_guessed == "i" or letters_guessed == "o" or letters_guessed == "u"):
            guesses_ramainings -= 2
        elif temp == get_guessed_word(secret_word, a):
            guesses_ramainings -= 1
        if get_guessed_word(secret_word, a) != temp:
            print("Good guess:", get_guessed_word(secret_word, a))
            temp = get_guessed_word(secret_word, a)
            print("-" * 26)
        else:
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, a))
            temp = get_guessed_word(secret_word, a)
            print("-" * 26)
        if is_word_guessed(secret_word, a) == True:
            print("Congratulations, you won! Your total score for this game is:", guesses_ramainings * len(set(secret_word)))
            break
        elif guesses_ramainings == 0:
            print("You lose:(\n Secret word:", secret_word)
        else:
            continue
        print()


q = ""
while q != "q":
    if __name__ == "__main__":

        #secret_word = choose_word(wordlist)
        #hangman(secret_word)


        secret_word = choose_word(wordlist)
        hangman_with_hints(secret_word)
        q = input("Press <<q>> to exit or any else button to restart game:\n")
