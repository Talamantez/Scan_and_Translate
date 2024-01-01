This script reads an image's text and translates it into another language
-----------------------------------------



Run with:  

python ./ocr_test.py
------------------------------------------
Example Output: 

OCR Russian:
ИЗБИРАТЕЛЬ:

Translated English:
voter

--------------------------------------------

OCR is performed with pytesseract:
Project description from pypi.org:
Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.

Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, including jpeg, png, gif, bmp, tiff, and others. Additionally, if used as a script, Python-tesseract will print the recognized text instead of writing it to a file.
