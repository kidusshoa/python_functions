def swap_numbers(a, b):
    a, b = b, a

    return a, b

a = 4
b = 6

a, b = swap_numbers(a, b)

print(f"After swapping:")
print(f"a is {a} and b is {b}")
