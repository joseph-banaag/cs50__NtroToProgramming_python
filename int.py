# interactive mode: run $ - python

result = int(input("What is your first number: ")) + int(input("What is your second number: "))
print(f"The result is: {result}")
# note: python will get what is inside the most inner parenthesis going to the most outer

# start of float data type
numb_1 = float(input("Enter your first number: "))
numb_2 = float(input("Enter your second number: "))

result = round(numb_1 + numb_2)
print(f"The result is: {result:,.2f}") # the :, adds the standard numbering for thousands separator and .2f is to show 2 decimal places after the period
# ***** END OF STRING AND INTEGERS
