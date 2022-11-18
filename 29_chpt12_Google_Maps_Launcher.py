'''
29 Google Maps Launcher
- user: copy the address we want to search for
- user: start the script
- take the address from clipboard
- launch the browser / Google Maps with the address
'''

import pyperclip as pc
import webbrowser

searchingFor = pc.paste()
sepSFor = searchingFor.split(' ')

link = 'https://www.google.co.uk/maps/search/'+ '+'.join(sepSFor)
webbrowser.open(link)