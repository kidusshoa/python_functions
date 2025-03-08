def count_character_types(string):
    lower_count = 0
    upper_count = 0
    digit_count = 0
    special_count = 0

    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1 
    return {
        "Lowercase count": lower_count,
        "Uppercase count": upper_count,
        "Numeric count": digit_count,
        "Special character count": special_count
    }

input_string = "@pyThOnlobb!Y34"
result = count_character_types(input_string)

print(f"Input String: {input_string}")
print(f"Numeric count: {result['Numeric count']}")
print(f"Lowercase count: {result['Lowercase count']}")
print(f"Uppercase count: {result['Uppercase count']}")
print(f"Special character count: {result['Special character count']}")
