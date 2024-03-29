def get_non_empty_input(prompt,validation=None):
    result = input(prompt)
    while not result or (validation and result not in validation):
        print(f"輸入不符合要求，請重新輸入：{', '.join(validation)}")
        result = input(prompt)
    return result