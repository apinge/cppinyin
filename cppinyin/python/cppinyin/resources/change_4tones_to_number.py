import re

def convert_tone_to_number(pinyin):
    # 将拼音中的声调转换为没有声调的字母和对应数字形式
    tone_map = {
        'ā': ('a', '1'), 'á': ('a', '2'), 'ǎ': ('a', '3'), 'à': ('a', '4'),
        'ē': ('e', '1'), 'é': ('e', '2'), 'ě': ('e', '3'), 'è': ('e', '4'),
        'ī': ('i', '1'), 'í': ('i', '2'), 'ǐ': ('i', '3'), 'ì': ('i', '4'),
        'ō': ('o', '1'), 'ó': ('o', '2'), 'ǒ': ('o', '3'), 'ò': ('o', '4'),
        'ū': ('u', '1'), 'ú': ('u', '2'), 'ǔ': ('u', '3'), 'ù': ('u', '4'),
        'ǖ': ('ü', '1'), 'ǘ': ('ü', '2'), 'ǚ': ('ü', '3'), 'ǜ': ('ü', '4')
    }

    # 使用正则表达式找到拼音音节
    syllables = pinyin.split()
    converted_pinyin = []

    for syllable in syllables:
        modified_syllable = ""
        tone_number = ""
        for char in syllable:
            if char in tone_map:
                base_char, tone = tone_map[char]
                modified_syllable += base_char
                tone_number = tone
            else:
                modified_syllable += char

        # 如果该音节有声调，添加数字表示
        if tone_number:
            modified_syllable += tone_number
        else:
            # 如果没有声调，则为轻声
            modified_syllable += '5'

        converted_pinyin.append(modified_syllable)

    return ' '.join(converted_pinyin)

# 读取 pinyin.raw 文件
with open('pinyin.raw', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

# 转换拼音并写入 cpp_pinyin.raw 文件
with open('cpp_pinyin.raw', 'w', encoding='utf-8') as outfile:
    for line in lines:
        parts = line.strip().split(' ', 2)
        if len(parts) == 3:
            chinese, score, pinyin = parts
            converted_pinyin = convert_tone_to_number(pinyin)
            outfile.write(f'{chinese} {score} {converted_pinyin}\n')

print(convert_tone_to_number("shǒu"))

print("Conversion complete. Saved as cpp_pinyin.raw.")
