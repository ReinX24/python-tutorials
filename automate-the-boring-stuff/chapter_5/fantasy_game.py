def display_inventory(inventory):
    """Print the items and values, also print total items."""
    total_item_count = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(f"{v} {k}")
        total_item_count += v
    print(f"Total number of items: {total_item_count}")


def add_to_inventory(inventory, added_items):
    """Add items in a list to a dictionary."""
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


if __name__ == "__main__":
    # inventory = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    inventory = {"gold coin": 42, "rope": 1}
    dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    inventory = add_to_inventory(inventory, dragon_loot)
    display_inventory(inventory)
