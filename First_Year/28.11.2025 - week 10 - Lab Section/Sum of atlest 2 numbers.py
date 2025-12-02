# Create a function that asks the user to enter numbers.
# The numbers must be whole (integers) and greater than 2.
# The user can enter numbers one by one.
# Entering '#' will stop the input process.
# If any number does not meet the condition, the function raises an error.
# If all numbers are valid, the function returns the sum of the numbers.

def sum_of_numbers ():
    list_for_sum = []

    while True:
        user_input = input("Enter numbers one by one (enter '#' when you are done):")

        if user_input == "#":
            break

        try:
            number = int(user_input)

            if number <= 0:
                raise ValueError ("Enter real numbers!")

            list_for_sum.append(number)

        except ValueError as verr:
            print(f"Error:{verr}\n")
    
    if len(list_for_sum) < 2:
        raise Exception("\nError: Not enough numbers for sum!\n")
    else:
        print("The sum of our numbers is:", sum(list_for_sum))


sum_of_numbers()