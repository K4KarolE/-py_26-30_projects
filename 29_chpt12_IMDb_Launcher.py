'''
29 IMDb Launcher - Chapter 12 - Practice
- user: copy the title (+ year of release) we want to search for
- user: start the script
- take the address from clipboard
- launch the browser / IMDb search result
'''

import pyperclip as pc
import webbrowser

searchingFor = pc.paste()

sep_title = searchingFor.split()

link = 'https://www.imdb.com/find?q=' + '+'.join(sep_title)

webbrowser.open(link)