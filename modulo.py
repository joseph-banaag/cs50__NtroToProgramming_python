# the parity symbols: (+,-,*,/,%)
# this program will determine even and odd numbers
# x = int(input("What is x? "))
# if x % 2 == 0:
#     print("the number is even")
# else:
#     print("the number is odd")

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("the number is even")
    else:
        print("the number is odd")

def is_even(n):
    return n % 2 == 0

main()