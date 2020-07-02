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

    # Game start, let the user know how many letters the secretWord contains
    print("Welcome to the game, Hangman!")
    secretWordLength = len(secretWord)
    print("I am thinking of a word that is %i letters long."%secretWordLength)

    # define lists
    lettersGuessed = []
    mistakesMade = []

    # Function to get guess
    def getGuess():
        print("-------------")
        # feedback to user
        print("You have %i guesses left." % (8-len(mistakesMade)))
        print("Available letters: " + getAvailableLetters(lettersGuessed))

        # Ask the user to supply one guess
        guess = input("Please guess a letter: ")

        # reject repeated guess
        while guess in lettersGuessed:
            print("Oops! You've already guessed that letter: "
                  + getGuessedWord(secretWord, lettersGuessed))
            return getGuess()

        # reject illegal guess
        while not str(guess).islower() or not len(str(guess)) == 1:
            print("Oops! That was an invalid guess. Please only guess a single"
                  + " lowercase alphabet")
            return getGuess()

        # record valid guess and feedback if it is correct
        lettersGuessed.append(guess)
        if guess not in secretWord:
            print("Oops! That letter is not in my word: "
                  + getGuessedWord(secretWord, lettersGuessed))
            mistakesMade.append(guess)
        else:
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        return None

    while not isWordGuessed(secretWord, lettersGuessed):
        getGuess()
        if len(mistakesMade) == 8:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was %s." %
                  secretWord)
            return None
    print("-------------")
    print("Congratulations, you won!")
    return None
