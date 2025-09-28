def main():
    with open("collected_names.csv") as file:
        for name in file:
             #   row = name.strip().split(",") # this is the usual way of assigning value to a variable
            person, house = name.strip().split(",") # assigning two variables at the same time with the use of .split() function
                # string.split(separator, maxsplit)
            print(f"{person} is in {house}")


if __name__ == "__main__":
    main()

"""
$$$ ASSIGNMENT:

    create a program that will find someone from the file and then throw a message if the person is not included.
"""


"""
with open("input_names.py") as file:
    for name in file:
        print(name)
        
"""