# coding=utf-8
import re
import string
import sys

arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
english_punctuations = string.punctuation
punctuations_list = arabic_punctuations + english_punctuations

arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida

                         """, re.VERBOSE)


def normalize_arabic(text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)
    return text


def remove_diacritics(text):
    text = re.sub(arabic_diacritics, '', text)
    return text


def remove_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)


def remove_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)


def usage():
    return "usage: python ", sys.argv[0] + "  <input file>  <output file>"

if __name__ == '__main__':
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        with open(input_file, encoding="utf-8") as file_reader, open(output_file, encoding="utf-8", mode='w') as file_writer:
            text = file_reader.read()
            text = remove_punctuations(text)
            text = remove_diacritics(text)
            text = remove_repeating_char(text)
            file_writer.write(text)
    else:
        print(usage())
