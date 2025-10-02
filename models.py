# models.py

class Directory:
    """
    Represents a directory with methods to create, list, and manage files.
    """
    def __init__(self, name):
        self.name = name

    def create(self):
        import os
        if not os.path.exists(self.name):
            os.makedirs(self.name)
            print(f"Directory '{self.name}' created.")
        else:
            print(f"Directory '{self.name}' already exists.")

    def list_files(self):
        import os
        if os.path.exists(self.name):
            files = os.listdir(self.name)
            if files:
                print(f"Files in '{self.name}':")
                for f in files:
                    print(f" - {f}")
            else:
                print(f"No files found in '{self.name}'.")
        else:
            print(f"Directory '{self.name}' does not exist.")

    def add_file(self, file_name, content=""):
        import os
        if not os.path.exists(self.name):
            print(f"Directory '{self.name}' does not exist.")
            return
        file_path = os.path.join(self.name, file_name)
        with open(file_path, "w") as f:
            f.write(content)
        print(f"File '{file_name}' added to '{self.name}'.")
