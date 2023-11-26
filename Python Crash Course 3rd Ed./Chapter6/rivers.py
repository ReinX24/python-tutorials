rivers = {
	'nile': 'egypt',
	'amazon': 'south america',
	'yangtze': 'eurasia',
}

for name, location in rivers.items():
	print(f"The {name.title()} runs through {location.title()}.")

# Printing each key and value in rivers dictionary
print("\nRivers:")
for name in rivers:
	print(name.title())

print("\nLocations:")
for location in rivers.values():
	print(location.title())