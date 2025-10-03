
for _ in range(8):
    with open("collected_names", "a") as file: # the file in as file is the return object just like the _ in for loop.
            # "a" and "+" is for appending and updating the file respectively
        file.write(input("What is your name? ").title() + "\n")



"""
open() syntax:
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

CODE FROM GOOGLE AI ASSISTANT

def collect_and_save_data(filename):
    # Collects user input and appends it to a specified file.
    print(f"Collecting data to {filename}. Enter 'exit' to stop.")

    while True:
        user_input = input("Enter data: ")
        if user_input.lower() == 'exit':
            break
        
        try:
            with open(filename, 'a') as file:
                file.write(user_input + '\n')
            print("Data appended successfully.")
        except IOError as e:
            print(f"Error writing to file: {e}")

# Call the function to start collecting data
collect_and_save_data('user_data.txt')

"""