from PIL import Image
import pytesseract
import numpy as np
from translate import Translator

def translateWord(word):
    result = ""
    try:
        result = translator.translate(word)
    except:
        result = "ERR"
    return result

def translateText(text):
    translated_text = []
    # Split into words
    wordArray = text.split()
    for word in wordArray:
        
        myWord = word.split(sep=",")[0]

        translated_word = translateWord(myWord)

        # print(translated_word)
        translated_text.append(translated_word)
    separator = " "
    return separator.join(translated_text)
        

# latin = 'lat', russian = 'rus', english = 'en'
source_lang = 'rus'
target_lang = 'en'
translator = Translator(to_lang=target_lang, from_lang=source_lang)
# get currently supported Tesseract OCR languages
# print(pytesseract.get_languages())

root = 'C:/Users/rober/Documents/Personal Projects/OCR/Scan_and_Translate/'
# filename = root + 'test_image_6.png'
filename = root + 'Screenshot_20231229_130556_Instagram.jpg'
# filename = root + 'test_image_2.png'
# filename = root + 'october.png'
# filename = root + 'march_17_russian_revolution_crop3.png'

# open the file
img1 = np.array(Image.open(filename))

# extract the text
# change lang in the following line to update the language
text = pytesseract.image_to_string(img1, lang=source_lang)

# Translator character count max is 500
print("Character Count: ")
print(len(text))

# Print OCR text
print("OCR " + source_lang.capitalize() + ":")
print(text)

# Print Translated text
print("Translated " + target_lang.capitalize() + ":")
print(translateText(text))
