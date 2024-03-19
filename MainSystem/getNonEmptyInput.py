def get_non_empty_input(prompt):
    result = input(prompt)
    while not result:
        result = input(prompt)
    return result