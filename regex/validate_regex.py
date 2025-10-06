import re

# TODO: the official regular expression for a syntactical valid email address for the modern browsers
official_pattern = ("^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]"
                    "+@"
                    "[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")

# syntax: re.search(pattern, string, flags=0)
email = input("What is your email address? ").strip()
pattern = r"^\w+@(\w+\.)?\w+\.(edu|com|net|gov|net)$"
        # this will match any word characters including special characters to the left and right of an @ sign and ends with the .edu TLD (top level domain)
        # the ? will be an option for optional characters to be matched so: (\w+\.)? will match word phrase and a dot. if the parenthesis is not present,
            #  the only optional is the dot after the \.


if re.search(official_pattern, email, re.IGNORECASE):
    print(f"VALID: the email address is: {email}")
else:
    print(f"ERROR: Invalid email address.")



# sample_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$"
# sample_pattern = r"^[^@]+@[^@]+\.edu$"

# metacharacters:
# . - match any character except a newline
# * - match 0 or more repetitions
# + - match one or more repetitions
# ? - match 0 or 1 repetition (it will match the word either it is present or not)
# {m} - match m repetitions
# {m,n} - match m-n repetitions
# ^ - will match from the start of the string
# $ - match at the end of the string
# [^@]+ - match all characters except @ and match one or more to the things to the left
# + - match one or more to the things to the left
# [^@]+@[^@]+ - this will match any characters from left and right of an @ sign except the @ sign. (there is only one @ sign in the string that will get matched)




# regex flags: re.IGNORECASE, re.DOTALL, etc...

# \d - match decimal digit
# \D - match not decimal digits
# \s - match whitespace characters
# \S - match the not whitespace characters
# \w - match word characters... as well as numbers and the underscore
# \W - match not a word character
# A|B - match either A or B
# (...) - match a group inside parenthesis
# (?:...) - match non-capturing version

# using regex for validation
# https://www.w3schools.com/python/python_regex.asp
# regex cheatsheet: https://www.datacamp.com/cheat-sheet/regular-expresso?utm_cid=19589720824&utm_aid=152984014694&utm_campaign=230119_1-ps-other~dsa~tofu_2-b2c_3-apac_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=20842-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~apac-en~dsa~tofu~cheat-sheet-data-science&gad_source=1&gad_campaignid=19589720824&gbraid=0AAAAADQ9WsEPCbdl8AP3RuBiINY-0tG02&gclid=Cj0KCQjw0Y3HBhCxARIsAN7931UbtPOLoZJL5jsiwnjLAWNb4iwbQBqeWh9Lh3Gx68qnLwEDn1vjG7QaAinhEALw_wcB
# if "@" in email and "." in email:
#     print(f"your email address: {email} is valid.")
# else:
#     print("Please put a valid email address.")

