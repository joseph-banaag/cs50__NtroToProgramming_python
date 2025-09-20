# dict for dictionary is a mutable, ordered collection of key-value pairs

houses = {
    "house_1": "Gryffindor",
    "house_2": "Slytherin"
}

for house in houses:
    print(f"{house} : {houses[house]}")

occupants = {
    "name_1": "Hermione",
    "name_2": "Harry",
    "name_3": "Ron",
    "name_4": "Draco"
}

for occu in occupants:
    print(f"{occu} : {occupants[occu]}")
    print(occu, occupants[occu], sep=" : ")



student_1 = houses["house_1"] + " " + occupants["name_1"]
print(student_1)

my_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "broccoli"]
}
#  THIS IS TO ACCESS THE ITEMS FROM THE LIST ITEMS INSIDE THE DICT
print(my_dict["vegetables"][0])

students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus":"Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russel Terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None
    },

]

for student in students:
    print(
        student["name"],
        student['house'],
        student['patronus'],
        sep=" → "
    )