import os
import random
import sys

words = [
  'potato','carrot','onion','tomatoe','peas','cabbage'
  ,'broccoli','celery','spinach','cucumber','turnip'
  ,'eggplant','kale','asparagus','lettuce','corn'
  ,'radish','garlic','leek','parsnip'
  ,'rhubarb','scallion','shallot','radicchio','wasabi','chicory'
  ]
hints = [
  'This vegetable is a key ingredient in crisps','A vegetable that is typically orange in color','This vegetable makes your eyes water',
  'This vegetable is a key ingredient in a sauce','This vegetable is green in color and found in a pod','A green vegtable thats a good source of potassium'
  ,'This vegetable looks like a small tree','celery','spinach','cucumber','turnip'
  ,'This vegetable is a deep purple color','A serving of this vegetable has more calcium than a small carton of milk.',
  'This vegetable can grow at one inch per hour ','This is a leaf like vegetable','This is a ceral crop'
  ,'This vegetable is typically consumed raw','This vegetable can cause bad breath','This vegetable goes well in potato soup',
  'This vegetable is closely related to carrots'
  ,'This vegetables stalk resemebles celery','This vegetable belongs to the same family as onions','This vegetable belongs to the same family as scallion',
  'This vegetable belongs to the daisy family','This vegetable belongs to the cabbage family','This vegetable belongs to the daisy family'
]
getHint = 'hint'



def clear():
    if os.name != 'nt':
        os.system('clear')
    else:
        os.system('cls')

def draw(badguess,goodguess,allguesses,word,amountOfGuesses):
    clear()
    print('Amount of guesses: {}/{}'.format(len(badguess),amountOfGuesses))
    print('')

    for letter in allguesses:
        print(letter,end=' ')
    print('\n\n')

    for letter in word:
        if letter in goodguess:
            print(letter,end='')
        else:
            print('',end='')
    print('')

def getguess(badguess,goodguess,allguesses,word):

    while True:

        guess = input("Guess a letter: ").lower()
        if guess == getHint:
            for index,item in enumerate(words):
                if item == word:
                    print(hints[index])
        elif len(guess) != 1 and guess != getHint:
            print("You can only guess one letter at a time")
        elif guess in badguess or guess in goodguess:
            print("You've already guessed that letter")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess

def play(done):

    badguess = []
    goodguess = []
    allguesses = []
    word = random.choice(words)
    clear()
    print('Choose your difficulty')
    mode = input(""" Type "Easy" for easy mode and "Hard" for hard mode: """).lower()
    if mode == 'hard':
        print('Hard mode selected')
        playgame = input("Press enter/return to Continue: ").lower()
        clear()
        if len(word) < 5:
            amountOfGuesses = 2
        elif len(word) < 8:
            amountOfGuesses = 3
        else:
            amountOfGuesses = 5

    else :
        print('Easy mode selected')
        playgame = input("Press enter/return to Continue: ").lower()
        clear()
        if len(word) < 5:
            amountOfGuesses = 3
        elif len(word) < 8:
            amountOfGuesses = 5
        else:
            amountOfGuesses = 7


    while True:

        draw(badguess,goodguess,allguesses,word,amountOfGuesses)
        guess = getguess(badguess,goodguess,allguesses,word)

        if guess in word:
            goodguess.append(guess)
            allguesses.append(guess)
            found = True
            for letter in word:
                if letter not in goodguess:
                    found = False
            if found:
                print("You win the word was {}.".format(word))
                done = True
        else:
            badguess.append(guess)
            allguesses.append(guess)
            if len(badguess) == amountOfGuesses:
                draw(badguess,goodguess,allguesses,word,amountOfGuesses)
                print("You lose the word was {}".format(word))
                done = True

        if done:
            playagain = input("Do you want to Play again? Y/N? ").lower()
            return play(done = False) if playagain.lower() != 'n' else exitGame()

def welcome():
    print('Welcome to veggie guesser a game where you guess the vegetable.')
    print("""Type "Hint" to get a hint about the word""")
    start = input("Press enter/return to Continue or Q to quit: ").lower()
    exitGame() if start.lower() == 'q' else  True


def exitGame():
    print("Thanks for playing")
    sys.exit()

done = False
while True:
    amountOfGuesses = 8
    clear()
    welcome()
    play(done)
