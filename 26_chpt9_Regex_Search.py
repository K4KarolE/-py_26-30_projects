'''
26 - Regex Search - Chapter 6 - Practice
- find phone number in a list
- find email address in a list
'''

import re

list = ['bubuka@gmail.com','bubu.pa@gmail.com','bubu-ta@gmail.com','Hey snake! What is your email address? Yesss, bubuka@gmail.comssss.''4',
        'bubuka_long@gmaillll.com', 'bubuka@gma00il.com', 'bubuka616@gmail.com', 'bubuka@gmail@.com@'
        '077 566 5654','077_566_5654', '0775665654','077-566-123', '077-566-5654', '077K566K5654'
        'random words', '554654654']

print()
print('Phone numbers:')
phoneNumRegex = re.compile(r'\d{3}.\d{3}.\d{4}')
for i in list:
    searchPN = phoneNumRegex.search(i)
    if phoneNumRegex.search(i):
        print(searchPN.group())
    # else:
    #     print('No match')
print('')

print('Emails:')
emailRegex = re.compile(r'''(
    [a-zA-Z0-9]+       #user name
    \@                 #@
    [a-zA-Z]+          #email host/provider
    \.                 #.
    [a-zA-Z]{2,4}      #extension
)''', re.VERBOSE)      #re.VERBOSE: allowing to visually separate logical sections of the pattern and add comments

for i in list:
    searchEmail = emailRegex.search(i)
    if emailRegex.search(i):
        print(searchEmail.group())
print('\n')
