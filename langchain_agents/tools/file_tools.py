import os


def create_file(file_name: str, content: str):
    with open(file_name, "w") as file:
        file.write(content)

    return f"{file_name} created successfully"


def update_file(file_name: str, content: str):
    with open(file_name, "a") as file:
        file.write("\n" + content)

    return f"{file_name} updated successfully"


def delete_file( file_name: str):
    if os.path.exists(file_name):
        os.remove(file_name)
        
        return f"{file_name} deleted"

    return "File not found"