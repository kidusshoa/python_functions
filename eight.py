def middle_character(string):
    length = len(string)
 
    mid = length // 2

    if length % 2 == 1:
        return string[mid]
    else:
        return string[mid - 1] + string[mid]

input_string1 = "Python"
input_string2 = "Programming"

result1 = middle_character(input_string1)
result2 = middle_character(input_string2)

print(f"The middle character(s) of \"{input_string1}\" is: \"{result1}\"")
print(f"The middle character(s) of \"{input_string2}\" is: \"{result2}\"")

