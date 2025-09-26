def main():

    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")



if __name__ == '__main__':
    main()

# THESE ARE THE SAMPLES OF DUNDER METHOD AND ATTRIBUTES
# print(__name__)
# print(__file__)

# these two prints will be called as well on import when run from the new file.