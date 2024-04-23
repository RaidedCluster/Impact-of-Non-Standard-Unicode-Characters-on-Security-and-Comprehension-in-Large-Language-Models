def enclosed_to_katakana(enclosed_str):
    enclosed_to_katakana_map = {
        '㋐': 'ア', '㋑': 'イ', '㋒': 'ウ', '㋓': 'エ', '㋔': 'オ',
        '㋕': 'カ', '㋖': 'キ', '㋗': 'ク', '㋘': 'ケ', '㋙': 'コ',
        '㋚': 'サ', '㋛': 'シ', '㋜': 'ス', '㋝': 'セ', '㋞': 'ソ',
        '㋟': 'タ', '㋠': 'チ', '㋡': 'ツ', '㋢': 'テ', '㋣': 'ト',
        '㋤': 'ナ', '㋥': 'ニ', '㋦': 'ヌ', '㋧': 'ネ', '㋨': 'ノ',
        '㋩': 'ハ', '㋪': 'ヒ', '㋫': 'フ', '㋬': 'ヘ', '㋭': 'ホ',
        '㋮': 'マ', '㋯': 'ミ', '㋰': 'ム', '㋱': 'メ', '㋲': 'モ',
        '㋳': 'ヤ', '㋴': 'ユ', '㋵': 'ヨ', '㋶': 'ラ', '㋷': 'リ',
        '㋸': 'ル', '㋹': 'レ', '㋺': 'ロ', '㋻': 'ワ', '㋼': 'ヰ',
        '㋽': 'ヱ', '㋾': 'ヲ', 
    }
    return ''.join(enclosed_to_katakana_map.get(char, char) for char in enclosed_str)

# Example usage
enclosed_str = """
㋕㋟㋕㋤
"""
katakana_str = enclosed_to_katakana(enclosed_str)
print(katakana_str)
