from PIL import Image
import os
from pathlib import Path
import pytesseract
import numpy as np
from translate import Translator

translator = Translator(to_lang='en', from_lang='rus')
# filename = 'C:/Users/rober/Documents/Personal Projects/OCR/Russian_Revolution/october.png'
filename = 'C:/Users/rober/Documents/Personal Projects/OCR/Russian_Revolution/march_17_russian_revolution_crop3.png'
img1 = np.array(Image.open(filename))
# change lang in the following line to update the language
text = pytesseract.image_to_string(img1, lang="rus")
print("OCR Russian: ")
print(text)
# extract each word

translated_text = translator.translate(text)
print("Translated English")
print(translated_text)
