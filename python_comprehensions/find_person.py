with open("people_extended.csv") as file:
    for name in file:
        print(name.split())



"""
    - assign the object where all names are accessible 
    - if creating a new object is redundant, try to access the names of the returned file object from open()
      
"""
