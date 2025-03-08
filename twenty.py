def square_numbers(lst):
  
    squared_list = [num ** 2 for num in lst]

    return squared_list

input_list = [2, 3, 4, 5, 6, 7, 8]
result = square_numbers(input_list)

print(f"Original List: {input_list}")
print(f"List with Squared Values: {result}")
