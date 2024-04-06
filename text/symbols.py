punctuation = ["!", "?", "…", ",", ".", "'", "-"]
pu_symbols = punctuation + ["SP", "UNK"]
pad = "_"

# korean
ko_symbols = [
    "ㄱ",
    "ㄴ",
    "ㄷ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅅ",
    "ㅇ",
    "ㅈ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
    "ㄲ",
    "ㄸ",
    "ㅃ",
    "ㅆ",
    "ㅉ",
    "ㅏ",
    "ㅓ",
    "ㅗ",
    "ㅜ",
    "ㅡ",
    "ㅣ",
    "ㅐ",
    "ㅔ"
]
num_ko_tones = 1

# combine all symbols
normal_symbols = sorted(set(ko_symbols))
symbols = [pad] + normal_symbols + pu_symbols
sil_phonemes_ids = [symbols.index(i) for i in pu_symbols]

# combine all tones
num_tones = num_ko_tones

# language maps
language_id_map = {"KO": 0}
num_languages = len(language_id_map.keys())

language_tone_start_map = {
    "KO": 0
}

if __name__ == "__main__":
    # a = set(zh_symbols)
    # b = set(en_symbols)
    print(sorted(a & b))
