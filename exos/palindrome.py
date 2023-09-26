def palindrome(word) :
#    if word == "".join(reversed(word)) :
#       return True
    if len(word) <= 1:
        return True
    else:
        if word[:1] == word[-1:]:
            return palindrome(word[1:-1])
        else:
            return False