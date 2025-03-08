def sum_of_digits(number):
    
    number_str = str(number)

    total_sum = 0
    
    for digit in number_str:
        total_sum += int(digit)
    
    return total_sum

input_number = 43521
result = sum_of_digits(input_number)

print(f"The sum of digits in {input_number} is: {result}")
