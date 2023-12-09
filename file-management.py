import os

def create_file(file_name, content=""):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File '{file_name}' created successfully.")

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    else:
        print(f"File '{file_name}' does not exist.")

def list_files(directory="."):
    files = os.listdir(directory)
    print(f"Files in '{directory}':")
    for file in files:
        print(file)

def create_directory(directory_name):
    os.makedirs(directory_name, exist_ok=True)
    print(f"Directory '{directory_name}' created successfully.")

def delete_directory(directory_name):
    if os.path.exists(directory_name):
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' deleted successfully.")
    else:
        print(f"Directory '{directory_name}' does not exist.")

# Example Usage
create_file("example.txt", "This is a sample file.")
list_files()

create_directory("example_folder")
list_files()

delete_file("example.txt")
list_files()

delete_directory("example_folder")
list_files()
