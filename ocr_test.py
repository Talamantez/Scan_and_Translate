from PIL import Image
import pytesseract
import numpy as np
from translate import Translator

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
    wordArray = text.split()
    for word in wordArray:
        
        myWord = word.split(sep=",")[0]

        translated_word = translateWord(myWord)

        # add the word to the output text
        translated_text.append(translated_word)
        
    # return the combined words    
    separator = " "
    return separator.join(translated_text)
        

# latin = 'lat', russian = 'rus', english = 'en', ukranian = 'ukr'
source_lang = 'rus'
target_lang = 'en'

# initialize translator
translator = Translator(to_lang=target_lang, from_lang=source_lang)

# get currently supported Tesseract OCR languages
# print(pytesseract.get_languages())

root = '/your_path/' 
# filename = root + 'latin_uxorem.png'
# filename = root + 'Screenshot_20231229_130556_Instagram.jpg'
# filename = root + 'greek_1.png'
filename = root + 'october.png'

# open the file
img1 = np.array(Image.open(filename))

# extract the text
text = pytesseract.image_to_string(img1, lang=source_lang)

# Print OCR text
print("\nOCR " + source_lang.capitalize() + ":")
print(text)

# Print Translated text
print("Translated " + target_lang.capitalize() + ":")
print(translateText(text))
