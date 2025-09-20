def square(x):
    return x *x

numbers = [1,2,3,4,5]

# apply the 'square' function to each number using map()
squared_numbers_map_object = map(square,numbers)
print(squared_numbers_map_object)
squared_numb_list = list(squared_numbers_map_object)
print(squared_numb_list)

# PYTHON MAP FUNCTION: https://www.w3schools.com/python/ref_func_map.asp

def myfunc(a,b):
    return a + b

x = map(myfunc, ("apple", "banana", "cherry"), ("orange", "lemon", "pineapple"))
new_list = list(x)
print(f"new list of fruits: {new_list}")