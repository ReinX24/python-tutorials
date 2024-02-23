def comma_code(generic_list):
    result_str = ""
    for index, item in enumerate(generic_list):
        if index != len(generic_list) - 1:
            result_str += f"{item}, "
        else:
            result_str += f"and {item}."
    return result_str


spam = ["apples", "bananas", "tofu", "cats"]
print(comma_code(spam))

spam = ["omen", "phoenix", "cypher", "viper"]
print(comma_code(spam))

print(comma_code([]))
