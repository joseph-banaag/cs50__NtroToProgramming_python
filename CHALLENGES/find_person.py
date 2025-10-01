with open("people_extended.csv") as file:
    for people in file:
        first_name,last_name,age,email,*address = list(people.split(","))
        print(first_name)
        print(last_name)
        print(age)
        print(email)
        print(*address)


        # print(len(list_people)) # this will display how many elements are in the row of people list
        # first_name,last_name,age,email,*address = list(people.strip().split(",")) # this will remove the space between people information
            # it will throw error when the "," separator is not defined.
            # *address will catch all remaining elements from the source

"""
PROBLEM:

    the problem with this approach is, the label from the csv file can be changed 
    but the variable created from this program won't be able to catch the same
    value from the csv if the file was rearranged. 
        - will be using csv.dictreader
        
"""