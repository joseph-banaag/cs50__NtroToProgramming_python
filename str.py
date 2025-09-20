# INITIAL LESSON:

name = input("What is your name? ")
print(f"Hello, {name}")
age = input("How old are you? ")
print(f"Awesome! {name}. You are doing great at {age}.")
"""
triple quotes can be used for multiple line comments
"""
# this is used for single line comment
print("this is to check if quotes will show in the terminal: 'hello' ")
print('this is to check "hello"')
print("back slash can also be used to display the quotes. and it is called \"escaping\"")

# name_1 = input(What is your name?")
# name = input("What is your name? ").strip()
# .strip() will remove white spaces from str
# name = name_1.strip() this will remove leading and trailing whitespaces
# name = name_1.capitalize() this will capitalized the very first letter of the string
# name = name_1.title() this will capitalize every first letter of the string
# name = name_1.title()
# name = name_1.strip().title()
name = input("What is your name? ").title().strip()
# print(f"Hello, {name}")
# age = input("How old are you? ")
# print(f"You are doing great {name} at age {age}.")

first, last = name.split(" ") #this will get the first name and last name as it was type respectively when the user input the value. it should be 2 values as well.
print(f"Hello, {first}")


# *****

name = input("what is your full name? ").title().strip()

first, last = name.split(" ")

print("First name: ",first,type(first))
print("Last name: ",last, type(last))

if last == "":
  print("no last name")
print(f"hello, {first}")

# *****

# *****     END OF STRING LESSON