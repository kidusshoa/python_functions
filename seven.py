def count_upper_lower(string):
  
    uppercase_count = 0
    lowercase_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count

input_string = "The quick Brow Fox"
upper_count, lower_count = count_upper_lower(input_string)

print(f"String: \"{input_string}\"")
print(f"No. of Upper case characters: {upper_count}")
print(f"No. of Lower case characters: {lower_count}")
