from collections import Counter

def char_count(word):
    character_counts = Counter(word)
    
    return dict(character_counts)

input_word = "programm"
result = char_count(input_word)

print(f"Input Word: {input_word}")
print(f"Occurrence of each character: {result}")
