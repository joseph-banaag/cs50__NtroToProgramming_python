# this program will display the functionality of match statement

name = input("What is your name? ").lower()

match name:
    case "harry" | "hermione" | "ron":
        print("gryffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who?")