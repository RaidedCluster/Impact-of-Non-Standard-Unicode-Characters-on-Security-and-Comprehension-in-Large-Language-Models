char_mapping = {
    'a': '◌ͣ', 'b': '◌ᷨ', 'c': '◌ͨ', 'd': '◌ͩ', 'e': '◌ͤ',
    'f': '◌ᷫ', 'g': '◌ᷚ', 'h': '◌ͪ', 'i': '◌ͥ', 'j': '?',
    'k': '◌ᷜ', 'l': '◌ᷝ', 'm': '◌ͫ', 'n': '◌ᷠ', 'o': '◌ͦ',
    'p': '◌ᷮ', 'q': '?', 'r': '◌ͬ', 's': '◌ᷤ', 't': '◌ͭ',
    'u': '◌ͧ', 'v': '◌ͮ', 'w': '◌ᷱ', 'x': '◌ͯ', 'y': '?', 'z': '◌ᷦ'
}

def map_string(input_string):
    # Use the mapping to transform the input string, character by character.
    # Characters not in the mapping will be left as is.
    return ''.join(char_mapping.get(char, char) for char in input_string.lower())

example_string = "HI"
mapped_string = map_string(example_string)
print(mapped_string)
