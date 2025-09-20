# $$$ DICTIONARY COMPREHENSION $$$
original_dict = {
    "a": 3,
    "b": 23,
    "c": 20
}

# MAP "VALUES" BY MULTIPLYING THEM BY 2
new_dict_value_mapped = {key:value * 2 for key,value in original_dict.items()}
print(new_dict_value_mapped)

# MAP "KEYS" BY CONVERTING THEM TO UPPERCASE
new_dict_key_converted = {key.upper():value for key,value in original_dict.items()}
print(new_dict_key_converted)

# MAP BOTH KEYS AND VALUES
new_dict_kv_mapped = {key.upper():value * 10 for key,value in original_dict.items()}
print(new_dict_kv_mapped)

# **** NEW DICTIONARY ****
print("\nBELOW THE ALL CAPS WILL BE PRINTED!")
dict_all_small = {
    "name" : "doks",
    "favorite": "mechanical keyboard",
    "favorite switch" : "thocky linear"
}

new_dict_all_caps = {key.upper():value.upper() for key,value in dict_all_small.items()}
print(new_dict_all_caps)

new_dict_all_title = {key.title():value.title() for key,value in dict_all_small.items()}
print(new_dict_all_title)

# combining the key and value from different variables
key_name = ["number_1", "number_2", "number_3"]
value_item = [3,23,20]

dict_from_kv = dict(zip(key_name,value_item))
print(dict_from_kv)
print("below is the combination of 3 lists")
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]
grades = ["A", "B", "A"]

# Zipping the lists together per indexes or per
combined_data = zip(names, scores, grades)

# Converting the zip object to a list to see the contents
list_of_tuples = list(combined_data)
print(list_of_tuples)
