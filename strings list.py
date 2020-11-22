# Test string for palindrome
# Palindrome is a string that reads the same
# forward and backward

def check_palindrome(word):
    word_backward = word[::-1]
    if word == word_backward:
        print("The words are palindrome")
    else:
        print("The words are not palindrome")

word = str(input(print("What words do you choose: ")))
check_palindrome(word)
