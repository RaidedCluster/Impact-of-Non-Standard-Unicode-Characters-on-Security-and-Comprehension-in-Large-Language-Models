import random

def scramble_text(text):
    char_map = {
        'A': '𝔸', 'B': '𝙱', 'C': 'ᴄ', 'D': '🅳', 'E': '🄴', 'F': '𝐅', 'G': '𝗚', 'H': '🅗', 'I': 'Ⓘ',
        'J': 'J̸̧̛̰̲̩͇̳͍̰̟͇͋̂̾͆̈́̑͝', 'K': 'ᴷ', 'L': 'ₗ', 'M': '𝑀', 'N': '𝑵', 'O': '𝖮', 'P': '𝙋', 'Q': '𝑄',
        'R': '𝗥', 'S': 'Ƨ', 'T': '𝓣', 'U': '𝒰', 'V': '𝖁', 'W': '𝔚', 'X': '🄧', 'Y': '🅨', 'Z': '🅩',
        'a': '𝐚', 'b': '𝗯', 'c': '⒞', 'd': '𝒅', 'e': '𝖊', 'f': '𝘧', 'g': '𝑔', 'h': '𝒉', 'i': '𝒾',
        'j': '𝒋', 'k': '𝖐', 'l': '𝔩', 'm': 'ᴍ', 'n': '𝓃', 'o': 'ⓞ', 'p': '⒫', 'q': '𝗾', 'r': '𝓇',
        's': 'ⓢ', 't': '⒯', 'u': '𝘂', 'v': '𝔳', 'w': 'ⓦ', 'x': '⒳', 'y': 'ⓨ', 'z': '⒵',
        '1': '1', '2': '𝟚', '3': '𝟹', '4': '𝟒', '5': '𝟱', '6': '⑥', '7': '⑺', '8': '⁸', '9': '₉',
        '10': '10'
    }

    randomized_case_text = ''.join(random.choice([char.upper(), char.lower()]) for char in text)

    # Scramble the text using the char_map
    scrambled_text = ''.join(char_map.get(char, char) for char in randomized_case_text)

    return scrambled_text

text = input("Enter eggs: ")
scrambled = scramble_text(text)
print(scrambled)
