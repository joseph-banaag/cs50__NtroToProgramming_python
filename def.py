# this function main is a convention to keep coding going down and not having to define a new function on top.
def main(): 
  name = input("What is your full name? ").strip().title()
  first_n, last_n = name.split(" ")

  hello(first_n)


        # the -to="friend" is the default value of the argument/parameter in hello function.
def hello(to="friend"): 
    print(f"Hello, {to}! How's it going?")




# THIS IS THE END OF THE MAIN FUNCTION
main()

def main():
  # """ function main is the scope region for passing parameter/argument """
  numb_1 = int(input("what's x: "))
  print(f"x squared is: {squared(numb_1)}")

def squared(n):
    return pow(n,2)

main()  

# **** THIS IS THE END OF THE FUNCTION LESSON

