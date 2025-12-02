# Create a function for user authorization.

# 1. The user enters a username and age.
# 2. This data is stored in a dictionary.
# 3. When the user enters a username, we check:
#    - If the username is an empty string, raise a ValueError: "No name provided".
#    - If the username is valid:
#       - If it already exists in the dictionary, print "Existing".
#       - Otherwise, ask for the age and check:
#           - Age must be an integer, positive, and greater than 12.
#           - If age is under the limit, print "Underaged".
#           - If age is valid, store the username and age, and return "Registered successfully".
# 4. A loop can then print all registered users.

def user_authorization():
    users = {}  # Store username: age

    while True:
        username = input("Enter username (or '#' to stop): ").strip()

        if username == "#":
            break

        # Username validation
        if username == "":
            raise ValueError("No name provided")

        # CASE 1 — New username → register
        if username not in users:
            print("New user, please register.")

            try:
                age_input = input("Enter your age: ")
                age = int(age_input)

                if age <= 0:
                    raise ValueError("Age must be positive")
                if age <= 12:
                    print("Underaged")
                    continue

                users[username] = age
                print("Registered successfully!")

            except ValueError as err:
                print("Invalid input:", err)
                continue

        # CASE 2 — Existing username → login
        else:
            print("Existing user. Please verify your age to log in.")
            try:
                age_input = input("Enter your age again: ")
                age = int(age_input)

                if age == users[username]:
                    print("Login successful!")
                else:
                    print("Wrong age!")

            except ValueError:
                print("Invalid age input.")

    # Print all users
    print("\nRegistered users:")
    for name, age in users.items():
        print(f"Username: {name}, Age: {age}")


# Run
user_authorization()
