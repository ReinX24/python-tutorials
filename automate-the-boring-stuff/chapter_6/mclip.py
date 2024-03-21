#! python3
# mclip.py - A multi-clipboard program.

import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

# When the user runs the file, 2 arguments are taken in. The first is the
# name of the file while the second one is the passed in argument to the file.
if len(sys.argv) < 2:
    print('Usage: python3 mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  # second argument stored user entered keyphrase
# The first argument is the file name (sys.argv[0] == mclip.py)

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")
else:
    print(f"There is no text for {keyphrase}.")
