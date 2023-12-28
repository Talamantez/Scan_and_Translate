from PIL import Image
import pytesseract
import numpy as np
from translate import Translator

# latin = 'lat', russian = 'rus', english = 'en'
source_lang = 'lat'
target_lang = 'en'
translator = Translator(to_lang=target_lang, from_lang=source_lang)
# get currently supported Tesseract OCR languages
# print(pytesseract.get_languages())

root = 'C:/Users/rober/Documents/Personal Projects/OCR/Scan_and_Translate/'
filename = root + 'test_image_6.png'
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

# Truncating
limit = 10
print('limiting character length to translate to ')
print(limit)
truncated_text = text[:limit] + '...' if len(text) > limit else text

print("OCR Latin: ")
print(text)

translated_text = translator.translate(truncated_text)
print("Translated English:")
print(translated_text)
