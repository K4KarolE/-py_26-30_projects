'''
29 Google Maps Launcher
- user: copy the address we want to search for
- user: start the script
- it takes the address from clipboard
- it launches Google Maps in a new browser tab displaying the direction between "your postcode" and the "target location"
'''

import pyperclip as pc
import webbrowser

searchingFor = pc.paste()

sepS_For = searchingFor.split()

your_postcode = "HP3+5BZ"       # example postcode

link = f'https://www.google.co.uk/maps/dir/{your_postcode}/' + '+'.join(sepS_For)

webbrowser.open(link)