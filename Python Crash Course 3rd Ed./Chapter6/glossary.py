glossary = {
	'pycharm': 'an integrated development environment for python',
	'variable': 'used to hold values',
	'integer': 'whole number representation',
	'double': 'holds a decimal value',
	'boolean': 'contains either true or false',
	'string': 'holds an array of characters',
	'lists': 'for storing multiple values',
	'set': 'stores data in an unordered sequence',
	'tuple': 'immutable list for storing values',
	'dictionary': 'for storing key value pairs',
}

# terms = glossary.keys()
# for term in terms:
# 	print(f"""{term.title()}:
# 	{glossary.get(term).capitalize()}.\n""")

# A much better way of printing our key value pairs
for term, definition in glossary.items():
	print(f"\n{term.title()}:")
	print(f"\t{definition.capitalize()}.")
