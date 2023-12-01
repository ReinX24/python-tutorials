from pathlib import Path

ask_name = True
file_path = Path('guest_book.txt')
entered_names = ''

while ask_name:
	guest_name = input('Enter your name (q to quit): ')
	if guest_name.lower() == 'q':
		ask_name = False
	else:
		entered_names += f"{guest_name}\n"

file_path.write_text(entered_names)
