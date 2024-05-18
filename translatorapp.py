from translate import Translator
print("Welcome to PrinceGuam's Translator!!")

desired_lang = input('What language do you want to translate to?: ')

translator = Translator(to_lang=desired_lang,from_lang='autodetect')

message = input('Enter the message you want to translate: ')

def lang_translator(text):
    translated = translator.translate(text)
    return translated

print(lang_translator(message))
