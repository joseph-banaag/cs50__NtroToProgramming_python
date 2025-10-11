import re

url = input("URL: ").strip()

if user_name4 := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE): # this conditional is using the walrus operator
    print(f"Username: {user_name4.group(3)}")



""" ***** some other ways of extracting username from twitter url ***** """
# username = url.replace("https://twitter.com/", "") # this method will remove the old value and replace it with new.
            # since the new value is empty, the old value will be removed leaving only the username from twitter url.

# username_2 = url.removeprefix("https://twitter.com/")

# re.sub syntax: re.sub(pattern, repl, string, count=0, flags=0)
# username_3 =  re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url, re.IGNORECASE) # escape the dot for the pattern so that regex would not mistake it as a different expression rather treat it as it is.
            # s in https will become optional since ? will allow with s or without s
            # () will group things
            # ? will make things optional

