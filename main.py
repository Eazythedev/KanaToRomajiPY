import MeCab

# Mapping table for kana to romaji conversion
kanaToRomaji = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    # ... Add more kana characters and their corresponding romaji
    "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
    # ... Add more katakana characters and their corresponding romaji
}

def convert_kana_to_romaji(kana):
    romaji = ""
    tagger = MeCab.Tagger("")
    node = tagger.parseToNode(kana)

    while node:
        if node.length > 0:
            kana_char = node.surface.decode("utf-8")
            if kana_char in kanaToRomaji:
                romaji += kanaToRomaji[kana_char]
        node = node.next

    return romaji

kana_input = "ひらがな カタカナ"
romaji_output = convert_kana_to_romaji(kana_input)
print(romaji_output)
