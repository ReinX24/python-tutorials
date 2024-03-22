#! python3 
# bulletPointAdder.py - Adds wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste() # store text on clipboard

# Separate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = f"* {lines[i]}"

text = '\n'.join(lines)

pyperclip.copy(text)
