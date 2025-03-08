def product_or_sum(num1, num2):
    
    product = num1 * num2

    if product > 500:
      
        return num1 + num2
    else:
        return product

input_num1 = 50
input_num2 = 12
result = product_or_sum(input_num1, input_num2)

print(f"Input Numbers: {input_num1}, {input_num2}")
print(f"Result: {result}")
