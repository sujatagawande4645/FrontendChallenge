import os

# Hard-coded username and password (replace with a secure method)
USERNAME = "admin"
PASSWORD = "password123"

def authenticate():
    attempts = 3
    while attempts > 0:
        username_input = input("Enter username: ")
        password_input = input("Enter password: ")

        if username_input == sujata and password_input == gawande:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed. Please try again.")
            attempts -= 1

    print("Too many failed attempts. Exiting.")
    return False

def create_file(file_name, content=""):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File '{file_name}' created successfully.")

# Other file management functions...C

# Main program
if authenticate():
    # Allow file management operations only if authentication is successful
    create_file("example.txt", "This is a sample file.")
    # Call other file management functions as needed
