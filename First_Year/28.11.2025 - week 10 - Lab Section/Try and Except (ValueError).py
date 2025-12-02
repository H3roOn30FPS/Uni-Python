# Create a function that asks the user for a number.
# The number must be a real, whole (integer) and positive value.
# If the condition is not met:
#     Return (or raise) a ValueError.
# If the condition is met:
#     Return "Bye-bye".


def checker_n ():
    user_input = input("Enter a number:")
    try:
        user_input = int(user_input)    

        if user_input <= 0:
             raise ValueError("Number cannot be negative or 0!\n")

        print("\nYour number is real and whole!\n")

    except ValueError as verr:
            print("\nRun time error:", verr)
                
    finally:
        print("Bye-bye!")

checker_n()