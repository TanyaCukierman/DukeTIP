from __future__ import print_function
import numpy
input=open("words_alpha.txt", 'r')
apples=input.read()
wordlist=apples.split("\n")
# Save this file using file saave in your browser
# Do not copy paste into PyCharm as it will mess up the indentation
# and thus your code will not run properly.

# Print Hangman's current state
def printHangman(numberWrong):
    if numberWrong==0:
        print("  _______")
        print(" |       |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_____")
    # TODO print top of noose
    if numberWrong == 1:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |")
        print(" |")
        print("_|_____")
        # TODO print head

        # TODO don't print head
    if numberWrong == 2:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |       |")
        print(" |")
        print("_|_____")
        # TODO print neck

        # TODO don't print neck
    if numberWrong == 3:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |")
        print("_|_____")
        # TODO print arms # Backslash is a spacial character so using two creates one

    if numberWrong == 4:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |       |")
        print("_|_____")
        # TODO print body

    if numberWrong == 5:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |       |")
        print("_|_____ /")
    # can't be > here so we get to the else :)
        # TODO print left leg
    elif numberWrong == 6:
        print("  _______")
        print(" |       |")
        print(" |       O")
        print(" |      /|\\")
        print(" |       |")
        print("_|_____ / \\")
        # TODO print both legs

        # TODO don't print any legs
    # TODO print bottom of noose

def printBlanks(word, correctLetters):
    solved=True
    # TODO Set solved equal to true (innocent until proven guilty)
    # TODO Loop over each letter in the word  for l in word:
    for l in word:

        l = l.lower() # not required but nice to have
        # Check if that letter is in the list of correct letters
        if l in correctLetters:
            print (l + " ", end="")
            # TODO If it is, print the letter and a space
        elif len(l)>1:
            print ("Please only input one letter")
        else:
            print ("_ ", end="")# TODO If it isn't, print an underscore and a space
            solved = False# TODO Also, set solved equal to False
    print()
    print()
    return solved


# TODO Define a list of words as options


#wordlist = ["tanya", "duke", "tip"]

# TODO Define a list to hold the correctly guessed letters

correctLetters = []

# TODO Define a variable to count the number of incorrect guesses
incorrectLetters = 0

# TODO Pick a random word to be used
word = numpy.random.choice(wordlist)


# TODO Print the Status of the Hangman (Hint: Call your function)
    
# TODO Print the word blanks and see if they solved it

solved = False
# Replace False with a function call
    
# TODO Catch Death (Exit loop if they got 6 or more wrong)
while True:
        printHangman(incorrectLetters)
        solved = printBlanks(word, correctLetters)

        if incorrectLetters == 6:
            print ("You Lose :(")
            break #stops the cycled

        if solved:
            print('You win!')
            break # no need to guess again

        # TODO Define a variable to hold user input
        l = ""
        # TODO Loop until they give a letter
        while l == "":
            l = raw_input("Guess a letter: ")
        # Check if the letter is in the word
        if l in word:
            correctLetters.append(l)
            # TODO Replace True with the correct condition
            # TODO If it's right, put it in the correct letters list and let them know it was right
        else:
            incorrectLetters=incorrectLetters+1
            # TODO If it's wrong, increment the wrong count and let them know it was wrong
        print()

# reveal the original word
print(word)