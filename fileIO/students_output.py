def main():
    with open("collected_names.csv") as file:
        for name in file:
            row = name.strip().split(",")
            # print(f"{row[0]} is in {row[1]}")
            print(f"{row[0]} is in {row[1]}")


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