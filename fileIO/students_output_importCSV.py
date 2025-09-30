import csv

def main():

    students = []
    with open("collected_names.csv") as file:
        reader = csv.reader(file)
        for name, home in reader: # this is the process of unpacking the file and assigning to a usable variables
            students.append({'name': name, 'home': home})

    for student in sorted(students, key=lambda people: people['name'], reverse=True):
        print(f"{student['name']} is in {student['home']}")


if __name__ == "__main__":
    main()