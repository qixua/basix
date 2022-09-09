from encrypt import encrypt

from classes.LanguageHandler import LanguageHandler

from lang.eng import english
from lang.fr import french
from lang.es import spanish
from lang.tr import turkish
from lang.lang_list import lang_list

BasixLangHandler = LanguageHandler(
    lang_list,
    {"english": english, "français": french, "español": spanish, "türkçe": turkish},
)

sections = BasixLangHandler.get_lang_and_text()

to_encrypt = input(f"{sections[0]}: ")
keymap_path = input(f"{sections[1]}: ")
encrypted = encrypt(to_encrypt, keymap_path)

print(f"{sections[2]}: {encrypted}")
