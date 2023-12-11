# Vim Motions Guide (2022)

#### h, j, k, l are different ways to traverse text
- h to go left
- j to go down
- k to go up
- l to go right

#### i to go into insert mode
I am currently learning about Vim motions using Neovim!

#### w and b to move one word at a time
I am moving one word at a time using w and b.
- w to move left, by one word, stops at commas, apostrophes, etc.
- b to move right, by one word, stops at commas, apostrophes, etc.
- W to move left by one word, does not stop at commas, etc.
- B to move right by one word, does not stop at commas, etc.

#### o to break into a new line after the cursor O to break into a new line above the cursor
This is some sample text.
This is some sample text.
This is some sample text.

#### % sign to go the the ending bracket or parenthesis
	(
		This is some text.
		This is some text.
		This is some text.
	)

function main() {
	console.log("This is some text")
}

#### { and } to jump between paragraphs

This is some sample text.
This is some sample text.
This is some sample text.

This is some sample text.
This is some sample text.
This is some sample text.

This is some sample text.
This is some sample text.
This is some sample text.

#### G to go to the bottom of the file and gg to go to the start
#### v to go into select mode
#### d to delete a line
#### u to undo last action
#### Ctrl V to select entire character 
#### y to copy text, p to paste text
#### p to paste after cursor, P to paste before cursor

#### D(capital) to delete all text inside and after the cursor

This is s
This is some sa
This is some sample text.

#### u to undo commands, ctrl r to redo commands

This is some sample text.
This is some sample text.
This is some sample text.

#### V to select a line and 5j to select 5 lines including highlighted line

This is some sample text.
This is some sample text.
This is some sample text.
This is some sample text.
This is some sample text.

#### v, selecting text, and pressing c will remove text and go into insert mode 
#### C(capital) to remove all text within and after cursor to go into insert mode

is some even more text!
This is some
This is some even more text!

#### d and $ to delete all text after a word
#### d and w to delete a single word (current word)
#### d and b to delete a single word (word before)
This is 
This is some even text!
This is some even more text!
