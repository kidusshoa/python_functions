import random
import string

def random_character():
    return random.choice(string.ascii_letters)  

def random_string(length=None):
    if length is None:
        length = random.randint(5, 10) 
    
    return ''.join(random.choices(string.ascii_letters, k=length)) 

char_result = random_character()
string_result = random_string()
fixed_length_string_result = random_string(8)

print(f"Random Character: {char_result}")
print(f"Random String (random length): {string_result}")
print(f"Random String (fixed length 8): {fixed_length_string_result}")
