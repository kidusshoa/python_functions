def unique_list(lst):
  
    unique_elements = list(set(lst))

    unique_elements.sort()

    return unique_elements

input_list = [1, 2, 3, 3, 3, 3, 4, 5]
result = unique_list(input_list)

print(f"Original List: {input_list}")
print(f"Unique List: {result}")
