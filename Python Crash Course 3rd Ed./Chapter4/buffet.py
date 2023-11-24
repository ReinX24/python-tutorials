buffet_foods = ('salad', 'shrimp', 'chicken', 'pork', 'crab')

print('Buffet Food Choices:')
for food in buffet_foods:
    print(f'# {food.title():10}')

# Rewriting the tuple
buffet_foods = ('burger', 'fries', 'chicken', 'pork', 'crab')

print('\nNew Buffet Food Choices:')
for food in buffet_foods:
    print(f'# {food.title():10}')
# Trying to modify one of the items in the tuple
# buffet_foods[0] = 'sausage' # throws an exception