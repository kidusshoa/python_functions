def count_occurrences(lst, value):
    occurrence_count = lst.count(value)

    return occurrence_count

input_list = [1, 3, 3, 4, 3, 2, 3]
search_value = 3

result = count_occurrences(input_list, search_value)

print(f"The value {search_value} occurs {result} times in the list.")
