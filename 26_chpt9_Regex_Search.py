'''
26 - Regex Search - Chapter 6 - Practice
- ask the user the route to the folder
- ask the user the regular expression the program should looking for
- print the result(file name and matches) to the screen
'''

'''
regex in list
regex in file
regex in folder

'''

import re

list = ['bubuka@gmail.com','bubu.pa@gmail.com','bubu-ta@gmail.com','4',
         '077 566 5654','077_566_5654', '0775665654','077-566-5654','random words', '554654654']

phoneNumRegex = re.compile(r'\d\d\d.\d\d\d.\d\d\d') #
for i in list:
    searchPN = phoneNumRegex.search(i)
    if phoneNumRegex.search(i):
        print(searchPN.group())
    else:
        print('No match')