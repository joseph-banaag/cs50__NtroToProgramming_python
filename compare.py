# conditional statement (<, >, <=, >=, ==, !=) will return True or False

x = int(input("What is x: "))
y = int(input("What is y: "))


if x < y:
    print(f"{x} is smaller than {y}")
elif x > y:
    print(f"{x} is bigger than {y}")
else:
    print(f"{x} is equal to {y}")

# eliminate another extra elif if the condition will fall on it as the last option.

# code below is just another way of comparing method to the shortest way
if x > y or x < y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")

# code below is the simplification of the code above. short is better.
if x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is not equal to {y}")
