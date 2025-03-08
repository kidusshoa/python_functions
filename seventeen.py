def sort_letters_by_case(string):

    lower_case_chars = [char for char in string if char.islower()]
    upper_case_chars = [char for char in string if char.isupper()]
    
    sorted_string = "".join(lower_case_chars + upper_case_chars)

    return sorted_string

input_string = "pytHOnloBBy"
result = sort_letters_by_case(input_string)

print(f"Original String: {input_string}")
print(f"Sorted String (Lowercase first, Uppercase after): {result}")
