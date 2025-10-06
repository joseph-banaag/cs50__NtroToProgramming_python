import re

# syntax: re.search(pattern, string, flags=0)
email = input("What is your email address? ").strip()
pattern = r"^[^@]+@.+\.edu$"
"""
^ - will match from the start of the string 
$ - match at the end of the string
[^@]+ - match all characters except @ and match one or more to the things to the left 
+ - match one ore more to the things to the left
"""

if re.search(pattern, email):
    print(f"the email address is valid: {email}")
else:
    print(f"ERROR: Invalid email address.")







# using regex for validation
'''
https://www.w3schools.com/python/python_regex.asp

if "@" in email and "." in email:
    print(f"your email address: {email} is valid.")
else:
    print("Please put a valid email address.")
'''

