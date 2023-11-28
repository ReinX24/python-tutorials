def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    person['age'] = age
    return person


musician = build_person("jimi", "hendrix", 27)
print(musician)
