def count_word_occurrences(text, word):
    words_list = text.split()

    occurrence_count = words_list.count(word)

    return occurrence_count

input_text = "john is a boy and john loves to play cricket."
search_word = "john"

result = count_word_occurrences(input_text, search_word)

print(f'The word "{search_word}" occurs {result} times in the given string.')
