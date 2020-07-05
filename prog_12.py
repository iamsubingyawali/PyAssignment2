def is_palindrome(word):
    reverse = ''.join(list(reversed(word)))
    if reverse.lower() == word.lower():
        return True
    else:
        return False


print(is_palindrome("Madam"))