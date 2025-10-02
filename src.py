# src.py

from models import Directory
from hfmodel import HFModel

def main():
    # Directory example
    dir_name = input("Enter directory name: ")
    my_dir = Directory(dir_name)
    my_dir.create()
    my_dir.list_files()
    my_dir.add_file("example.txt", "Hello World!")
    my_dir.list_files()

    # HFModel example
    model = HFModel("TestModel", "1.0")
    data = [1, 2, 3, 4]
    result = model.run_model(data)
    print("Model result:", result)

if __name__ == "__main__":
    main()

