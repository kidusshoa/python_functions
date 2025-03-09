def remove_duplicates(string):
    unique_chars = []
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
    return "".join(unique_chars)

input_string = "pythonlobby"
result = remove_duplicates(input_string)

print(f"Original String: {input_string}")
print(f"String after removing duplicates: {result}")
