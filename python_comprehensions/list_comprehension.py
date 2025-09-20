# LIST COMPREHENSION SYNTAX:
# newlist = [expression for item in iterable if condition == True]

#  *** this is the longest version ***
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)

# *** this is the shortest version ***
squares = [x**2 for x in range(5)]
print(squares)


fruits = ["banana", "apple", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        print(x)

numbers = [1,2,3,4,5,6,7,8,9,10]
show_even = [num for num in numbers if num % 2 == 0]
print(show_even)

words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

matrix = [
    [1,2],
    [3,4,5]
]
flattened_list = [num for row in matrix for num in row]
print(flattened_list)

fruits = ["banana", "apple", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

newList_v2 = [fruit for fruit in fruits]
print(f"This is the new list version 2: {newList_v2}")

# one line with condition
newList_v3 = [prutas for prutas in fruits if "a" in prutas]
print(f"this version has condition: {newList_v3}")


# w3 school list comprehension
# https://www.w3schools.com/python/python_lists_comprehension.asp