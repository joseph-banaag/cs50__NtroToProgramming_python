score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score > 90:
    print("Grade B:")
elif 70 <= score > 80:
    print("Grade C:")
else:
    print("Grade D:")

# this is the simplified approach to the conditionals

if score >= 90:
    print("Grade A: ")
elif score >= 80:
    print("Grade B:")
elif score >= 70:
    print("Grade C:")
else:
    print("Grade D:")