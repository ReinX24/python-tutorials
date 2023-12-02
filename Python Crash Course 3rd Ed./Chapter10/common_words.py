from pathlib import Path


def count_words(file_path, text_match):
    """Count the matching words inside a text file."""
    try:
        contents = file_path.read_text().lower().split()
        print(contents.count(text_match))
    except FileNotFoundError:
        print(f"{file_path} not found!")


# Finding how much 'the' is used in the text file
search_text = 'the'
files = ['moby_dick.txt', 'little_women.txt', 'the_file.txt']
for file in files:
    count_words(Path(file), search_text)
