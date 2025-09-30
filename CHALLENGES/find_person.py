with open("people_extended.csv") as file:
    for people in file:
        # print(len(list_people)) # this will display how many elements are in the row of people list
        # first_name,last_name,age,email,*address = list(people.strip().split(",")) # this will remove the space between people information
        first_name,last_name,age,email,*address = list(people.split(","))
            # it will throw error when the "," separator is not defined.
            # *address will catch all remaining elements from the source
        print(first_name)
        print(last_name)
        print(age)
        print(email)
        print(*address)




"""

    assignment:
        - create a program that will find people from a list
        
"""