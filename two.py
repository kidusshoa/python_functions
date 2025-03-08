def swap_case(input_string):
    
    swapped_string = ""
  
    for char in input_string:
        if char.isupper():
            swapped_string += char.lower()
        elif char.islower():
            swapped_string += char.upper()
        else:
            swapped_string += char

    return swapped_string

input_string = "PrOgRaMM"
result = swap_case(input_string)


print(f"Original String: {input_string}")
print(f"Swapped Case String: {result}")
