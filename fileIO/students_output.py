def main():

    students = []
    with open("collected_names.csv") as file:
        for name in file:
            person, house = name.strip().split(",")

            student = {"name": person, "house": house}  # this is to create a new dict using the keys and values from the source file
            students.append(student)

        for student in sorted(students, key=lambda people: people['name'], reverse=True):
            print(f"{student['name']} is in {student['house']}")

"""
    Note:  
        this is the long way of creating a new dictionary from the source file.
            student = {}
            student["name"] = person
            student["house"] = house
"""



"""
    note: the iterable source file was converted to list first before sorting by key
    sorted() function syntax:
        sorted(iterable, key=key, reverse=reverse)
    
"""


if __name__ == "__main__":
    main()