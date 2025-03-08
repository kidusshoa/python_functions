def filter_even_odd(lst):
   
    even_numbers = []
    odd_numbers = []

   
    for num in lst:
        if num % 2 == 0: 
            even_numbers.append(num)
        else:  
            odd_numbers.append(num)

    return even_numbers, odd_numbers

input_list = [2, 23, 24, 51, 46, 67]
even_list, odd_list = filter_even_odd(input_list)

print(f"Original List: {input_list}")
print(f"Even Numbers: {even_list}")
print(f"Odd Numbers: {odd_list}")
