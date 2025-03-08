def sum_list(numbers):
   
    total_sum = 0
   
    for num in numbers:
        total_sum += num
    
    return total_sum

input_list = [8, 2, 3, 0, 7]
result = sum_list(input_list)

print(f"The sum of the numbers in the list {input_list} is: {result}")
