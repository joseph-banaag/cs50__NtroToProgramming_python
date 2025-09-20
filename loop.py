def main():
    i = 3
    # WHILE LOOP
    while i != 0:
        print(f"counting starts in: {i}")
        i -= 1
    print(f"end of the counting: {i}")

    while True:
        n = int(input("What is n? "))
        if n > 0:
            # this will be true and the code will run again if the value of n does not follow the condition
            break

    print("end of the program!")

# ***********
    # FOR LOOP
    for a in [0,1,2]:
        print(f"counting starts in: {a} for the letter (a)")

    for _ in range(5):
        print(f"range counting starts in: {_} (_ is a placeholder variable)")

# ****************************************
# def main():
#     below is the program that will get a number from the user and will continue asking for the number if -
    #     the condition for numb > 0 has not met.
    number_frm_user = ask_user()
    count_numb(number_frm_user)

def ask_user():
    while True:
        numb = int(input("What is the number? "))
        if numb > 0:
            break
    return numb


def count_numb(n):
    for _ in range(n):
        print(f"count down in: {_}")

if __name__ == "__main__":
    main()

"""
    *** START OF NOTE ***
    
    
    *** the other way of writing and considering 0 as the initial value
    i = 0
    
    while i < 3:
        print(f"countdown in: {i}")
        i += 1
        
    range() parameters:
        range(5) - the default increment is 1 from zero and the specified number is not included. 0-4
        range(2-5) - it will start from the specified starting value and end in 4
        range(3,30,3) - starting value, end value, and the specified increment which is by 3 up to 29
        
    *** END OF NOTE ***

"""

# *************** SOME FOR LOOP SAMPLES **********

fruits = ["apple", "banana", "cherry"]

for f in fruits: # or for fruit in fruits
    print(f"{f}")
    #  print(f)

word = "Python"
for char in word:
    print(char) # this will display every letter from the value of the given variable

for i in range(5):
    print(i) # this will loop from 0 to 4

for i in range(2,8):
    print(i) # this will loop from 2 to 7 (last number is exclusive)

for i in range(0,10,2):
    print(i) # this will loop from 0 to 9 increment by 2

# NESTED FOR LOOP SAMPLES
for i_1 in range(5):
    for i_2 in range(3):
        print(f"i_1: {i_1}, i_2: {i_2}")

# FOR LOOP WITH ELSE BLOCK
for i in range(5):
    print(i)
else:
    print("loop is finished!")

# FOR LOOP WITH BREAK AND CONTINUE STATEMENTS

for i in range(10):
    if i==5:
        break # this will terminate the loop when i- is 5.
    if i % 2 == 0:
        continue # this will skip even numbers.
    print(i)

# LIST COMPREHENSION:

squares = [x**2 for x in range(5)]
print(squares)