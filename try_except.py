# while True:
#     try:
#         x = int(input(Please enter a number: )) # this line creates the ValueError if the user entered not a number
#     except ValueError:
#         print("It is not an integer!")
#     else:
#         break
#
# print(f"You gave the number: {x}")

def main():
    x = get_numb()
    print(f"the number is: {x} from x")

    y = get_numb_2("Please enter a number: ")
    print(f"the number is: {y} from y")

# *** THIS IS THE LONGER VERSION ***
def get_numb():
    while True:
        try:
            x = int(
                input("Please enter a number: "))  # this line creates the ValueError if the user entered not a number
        except ValueError:
            print("It is not an integer!")
        else:
            break
    #     note: break can be omitted and replaced with return since it will also break the loop and return the value of x
    return x

# *** THIS IS THE SHORTER VERSION ***
# explanation: this function will return what was asked from the input()
# pythonic way of writing code is making sure the program work and then add except just to eliminate the error and continue with the program.
# unlike other language like JS or TS that requires error prompting the user, python can just have the except and then let the program run again

def get_numb_2(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


if __name__ == '__main__':
    main()