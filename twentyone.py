def remove_duplicates(lst):
    unique_list = []

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

input_list = [2, 3, 4, 5, 2, 6, 3, 2]
result = remove_duplicates(input_list)

print(f"Original List: {input_list}")
print(f"List after Removing Duplicates: {result}")
