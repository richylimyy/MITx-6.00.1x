def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    display = ""
    for let in secretWord:
        if let in lettersGuessed:
            display += let
        else:
            display += "_ "
    return display
