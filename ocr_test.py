from PIL import Image
import pytesseract
import numpy as np
from translate import Translator
from colorama import Fore

# Read your target path from 'my_path.txt'
my_path = open("my_path.txt").read()

# List of languages:
# ['afr', 'amh', 'ara', 'asm', 'aze', 'aze_cyrl', 'bel', 'ben', 'bod', 'bos', 'bre', 'bul', 'cat', 'ceb', 'ces', 'chi_sim', 'chi_sim_vert', 'chi_tra', 'chi_tra_vert', 'chr', 'cos', 'cym', 'dan', 'deu', 'div', 'dzo', 'ell', 'eng', 'enm', 'epo', 'equ', 'est', 'eus', 'fao', 'fas', 'fil', 'fin', 'fra', 'frk', 'frm', 'fry', 'gla', 'gle', 'glg', 'grc', 'guj', 'hat', 'heb', 'hin', 'hrv', 'hun', 'hye', 'iku', 'ind', 'isl', 'ita', 'ita_old', 'jav', 'jpn', 'jpn_vert', 'kan', 'kat', 'kat_old', 'kaz', 'khm', 'kir', 'kmr', 'kor', 'lao', 'lat', 'lav', 'lit', 'ltz', 'mal', 'mar', 'mkd', 'mlt', 'mon', 'mri', 'msa', 'mya', 'nep', 'nld', 'nor', 'oci', 'ori', 'osd', 'pan', 'pol', 'por', 'pus', 'que', 'ron', 'rus', 'san', 'sin', 'slk', 'slv', 'snd', 'spa', 'spa_old', 'sqi', 'srp', 'srp_latn', 'sun', 'swa', 'swe', 'syr', 'tam', 'tat', 'tel', 'tgk', 'tha', 'tir', 'ton', 'tur', 'uig', 'ukr', 'urd', 'uzb', 'uzb_cyrl', 'vie', 'yid', 'yor']

def translateWord(word):
    result = ""
    try:
        result = translator.translate(word)
    except:
        result = "-"
    return result

def translateText(text):
    translated_text = []
    
    # Split into words
    word_array = text.split()
    for word in word_array:
        
        myWord = word.split(sep=",")[0]

        translated_word = translateWord(myWord)

        # add the word to the output text
        translated_text.append(translated_word)
        
    # reconstruct the text    
    separator = " "
    return separator.join(translated_text)  

def compare(text, translated_text):
    # see if the index in 'translated_text' is equal to a failure indicator (using a "-")
    # if so, print red , if not print green
    
    # Split into words
    word_array = text.split()
    translated_word_array = translated_text.split()

    # Print OCR words highlighting translation successes
    print(Fore.LIGHTCYAN_EX, "\nOCR " + source_lang.capitalize() + ":")
    for word in word_array:
        if word_array.index(word) <= len(translated_word_array):
        
            if translated_word_array[word_array.index(word)] == '-':
                print(Fore.RED, word, end='')
            else:
                print(Fore.GREEN, word, end='')

    # Print Translated words highlighting translation successes
    print(Fore.LIGHTCYAN_EX, "\nOCR " + target_lang.capitalize() + ":")
    for translated_word in translated_word_array:
        if translated_word == '-':
            print(Fore.RED, translated_word, end='')
        else:
            print(Fore.GREEN, translated_word, end='')

    print(Fore.WHITE, "\nEND")
# latin = 'lat', russian = 'rus', english = 'en', ukranian = 'ukr', greek = 'grc'
source_lang = 'grc'
target_lang = 'en'

# initialize translator
translator = Translator(to_lang=target_lang, from_lang=source_lang)

# get currently supported Tesseract OCR languages
# print(pytesseract.get_languages())

root =  my_path
# filename = root + 'latin_uxorem.png'
# filename = root + 'Screenshot_20231229_130556_Instagram.jpg'
# filename = root + 'greek_3.png'
# filename = root + 'october.png'
filename = root + 'greek_3.PNG'

# open the file
img1 = np.array(Image.open(filename))

# extract the text
text = pytesseract.image_to_string(img1, lang=source_lang)

# Print OCR text
# print("\nOCR " + source_lang.capitalize() + ":")
# print(text)

# Print Translated text
# print("Translated " + target_lang.capitalize() + ":")
translated_text = translateText(text)
# print(translated_text + "\n")

# Print text again highlighting word translation successes and failures
# Based on index 
compare(text,translated_text)
