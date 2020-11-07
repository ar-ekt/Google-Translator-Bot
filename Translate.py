from Consts import *

from googletrans import Translator

translator = Translator()

def translate(text: str, source: str=EN, destination: str=FA):
    try:
        translated_text = translator.translate(text, src=source, dest=destination)
        return translated_text
    except:
        return False

def inline_translate(text: str, source: str=EN, destination: str=FA) -> str:
    if text == "":
        return text
    while True:
        translated = translate(text, source, destination)
        if translated != False:
            return translated.text