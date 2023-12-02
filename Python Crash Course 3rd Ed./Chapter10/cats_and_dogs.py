from pathlib import Path


def read_file(file_path):
    """Read the contents of a text file"""
    try:
        contents = file_path.read_text()
    except FileNotFoundError:
        # print(f"\n{file_path} not found!")
        pass
    else:
        print(f"\n{file_path}: ")
        print(contents)


files = ['cats.txt', 'dogs.txt']
for file in files:
    path = Path(file)
    read_file(path)
