def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ans = ""
    for let in "abcdefghijklmnopqrstuvwxyz":
        if let not in lettersGuessed:
            ans += let
    return ans
