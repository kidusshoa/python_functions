def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    
    return fahrenheit

input_celsius = 10
result_fahrenheit = celsius_to_fahrenheit(input_celsius)

print(f"{input_celsius:.1f} Celsius is equal to {result_fahrenheit:.1f} Fahrenheit")
