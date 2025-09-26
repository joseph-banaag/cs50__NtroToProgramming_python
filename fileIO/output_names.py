with open("collected_names.txt") as file:
    for name in sorted(file):
        print(f"hello, {name.strip()}")


"""
    # this is another way of writing the code
    
names = []

with open("collected_names.txt") as file: # by default, open is set to "r" as read
    for name in file:
        names.append(name.strip())
for person in sorted(names): # sorted() since a function, can be applied to any iterable.
    print(f"hello, {person}")
    
    # end of program
"""


"""


names.sort() # this .sort() only applies on list 
for person in names:
    print(f"hello, {person}")
    
    
"""



"""
    # persons = file.read()
    persons = file.readlines()

for person in persons:
    name = person.strip()
        # if the strip is not applied, the printout will have a new line since we have \n from the file itself
    print(f"hello, {name}")
    
    .strip() - will remove whitespaces and characters like \n from each side of the string
    .rstrip() - will remove whitespaces and characters from the right of the string
    .lstrip() - will remove whitespaces and characters from the left of the string
    
"""

