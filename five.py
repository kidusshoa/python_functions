def is_even_or_odd(number):
    
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

input_number = 7
result = is_even_or_odd(input_number)

print(f"The number {input_number} is: {result}")
