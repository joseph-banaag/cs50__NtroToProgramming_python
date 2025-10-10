import re

name = input("What's your name?\n").strip() # this is the convention for making sure there is no whitespace that might be accidentally added during sign up

pattern = r"^(.+), ?(.+)$" # this will check for space after comma, but it'll include extra spaces in the output.
pattern_2 = r"^(.+), *(.+)$" # this will result differently when dealing with white spaces

if validate_name := re.search(pattern_2, name): # this operation is using the walrus operator
                # walrus operator is used when it is only needed to check a True or False condition
    name = validate_name.group(2) + " " + validate_name.group(1) # this will display firstname and lastname

print(f"Hello, {name}")

