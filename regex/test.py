import re

pattern =r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+/.eu$"
    #r"^[^@]+@[^@]+$" # this will match any characters from the left and right of an @ sign. There should be only one @ sign in the string.

string_test = input("What is the string?\n")

if re.search(pattern, string_test):
    print(f"the string: {string_test} is a match and valid entry! ")
else:
    print("ERROR: Invalid entry.")

