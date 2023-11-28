def sandwich_ingredients(*ingredients):
    """Accepts ingredient's for a sandwich"""
    print(f"\n[Sandwich Ingredients]")
    for ingredient in ingredients:
        print(f"- {ingredient}")


# Continue at page 150
sandwich_ingredients('cheese')
sandwich_ingredients('strawberry jam', 'peanut butter')
sandwich_ingredients('ham', 'cheese', 'mayonnaise')
