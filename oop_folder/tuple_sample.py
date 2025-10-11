def main():
            # this is using a tuple with a different way of parsing or unpacking the data from the function
    name, house = get_student()
    print(f"Name:\n -{name}\nHouse:\n -{house}")

            # this is using a tuple
    student_info = get_student()
    print(f"Name:\n -{student_info[0]}\nHouse:\n -{student_info[1]}")
            # this is using a tuple
    name, age, city = get_user_information()
    print(f"Name: -{name}\nAge: -{age}\nCity: -{city}")

        # this is using the dict
    student = get_student_info()
    print(f"Name: -{student['name']}\nAge: -{student['age']}\nCity: -{student['city']}")


# using tuple
def get_student():
    name = input("What is your name?\n")
    house = input("Where do you live?\n")
    return name, house
# using tuple
def get_user_information():
    name = input("What is your name?\n")
    age = input("How old are you?\n")
    city = input("Where do you live?\n")
    return name, age, city

# using dict
def get_student_info():
    return {"name": input("What your name?\n"), "age": input("How old are you?\n"), "city":input("Where do you live?\n")}


if __name__ == '__main__':
    main()



