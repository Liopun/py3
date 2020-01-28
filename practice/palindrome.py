# Q6:


def pal_finder(str_og):
    # put in lower cases using casefold()
    str_og = str_og.casefold()

    # turn the returned reversed object into a string
    str_nu = ''.join(reversed(str_og))
    # better performance but not self-explanatory
    # str_nu = str_og[::-1]

    status = list(str_og) == list(str_nu)
    return str_nu, status


try:
    word_og = str(input("Palindrome Checker \nEnter a string: "))
    word_nu, status = pal_finder(word_og)
    print("Original Word: %s \nNew Word: %s \nPalindrome Status: %s" % (word_og, word_nu, status))
except ValueError as e:
    print("Invalid input", e)
except Exception as e:
    print("Error occurred", e)
