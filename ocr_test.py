from PIL import Image
import pytesseract
import numpy as np
from translate import Translator
import re


source_lang = 'lat'
target_lang = 'en'
translator = Translator(to_lang=target_lang, from_lang=source_lang)
# get currently supported Tesseract OCR languages
# print(pytesseract.get_languages())
# filename = 'C:/Users/rober/Documents/Personal Projects/OCR/Russian_Revolution/test_image.png'
filename = 'C:/Users/rober/Documents/Personal Projects/OCR/Russian_Revolution/test_image_2.png'
# filename = 'C:/Users/rober/Documents/Personal Projects/OCR/Russian_Revolution/october.png'
# filename = 'C:/Users/rober/Documents/Personal Projects/OCR/Russian_Revolution/march_17_russian_revolution_crop3.png'

# open the file
img1 = np.array(Image.open(filename))

# extract the text
# change lang in the following line to update the language
text = pytesseract.image_to_string(img1, lang=source_lang)

# Translator character count max is 500
print("Character Count: ")
print(len(text))

# Truncating
limit = 10
truncated_text = text[:limit] + '...' if len(text) > limit else text

print("OCR Latin: ")
print(text)

translated_text = translator.translate(truncated_text)
print("Translated English")
print(translated_text)
