'''
Google Translate Launcher - ENG/HUN
'''

import pyperclip as pc
import webbrowser

text = pc.paste()

lang_from = 'en'
lang_to = 'hu'

link = f'https://translate.google.com/?sl={lang_from}&tl={lang_to}&text={text}'

webbrowser.open(link)