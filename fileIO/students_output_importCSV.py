import csv

def main():
    students = []

    with open("../CHALLENGES/people_extended.csv", "r", newline="") as csvFile: # the file has the header that will be the reference for the keys.
        reader = csv.DictReader(csvFile)
        for row in reader:
            students.append({'first_name': row['First Name'], 'last_name': row['Last Name'], 'age':row['Age'], 'email' : row['Email'] , 'address': row['Address']})

    for student in sorted(students, key=lambda s: s["first_name"] ):
        print(f"{student["first_name"]} is from {student["address"]}")

if __name__ == "__main__":
    main()