import os

class FileManagementTool:

    def create_file(self, file_name, content):
        with open(file_name, "w") as file:
            file.write(content)

        return f"\n{file_name} created"

    def update_file(self, file_name, new_content):
        with open(file_name, "a") as file:
            file.write("\n" + new_content)

        return f"{file_name} updated"

    def delete_file(self, file_name):
        if os.path.exists(file_name):
            os.remove(file_name)

            return f"{file_name} deleted"

        return "File not found"