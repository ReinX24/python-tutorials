if __name__ == "__main__":
    cat_names = []
    while True:
        print(
            f"Enter the name of cat {len(cat_names) + 1} (Or enter nothing to stop.):"
        )
        new_cat_name = input()
        if new_cat_name == "":
            break
        cat_names.append(new_cat_name)

    print("The cat names are:")
    for name in cat_names:
        print(f"\t{name}")
