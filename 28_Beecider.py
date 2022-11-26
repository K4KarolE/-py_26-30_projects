#!/usr/bin python3.11

'''
28 - Beecider - Motion Picture Details Scraping Decider
- details scraping for: TV Movie, TV Special (project 27)// Movies (project 22) // TV Series (project 23)
- instead of starting one of the 3 programs according of the new record`s type
- start only one, which triggers the chosen one
'''

from subprocess import call
import os, platform, shutil

terminal_columns = shutil.get_terminal_size().columns

def run_Movie():
    if platform.system() == 'Windows':
        os.chdir(r"D:\_DEV\Python\py_21-25_projects")
        call(["python", "22_Movie_Details_Scraping.py"])
    if platform.system() == 'Linux':
        os.chdir(r"/home/zsandark/_DEV/Python/py_21-25_projects")
        call(["python3.11", "22_Movie_Details_Scraping_CP.py"])

def run_Series():
    if platform.system() == 'Windows':
        os.chdir(r"D:\_DEV\Python\py_21-25_projects")
        call(["python", "23_TVShow_Details_Scraping.py"])
    if platform.system() == 'Linux':
        os.chdir(r"/home/zsandark/_DEV/Python/py_21-25_projects")
        call(["python3.11", "23_TVShow_Details_Scraping_CP.py"])

def run_TV_Movie_TV_Special():
    if platform.system() == 'Windows':
        os.chdir(r"D:\_DEV\Python\py_26-30_projects")
        call(["python", "27_TVMovie-TVSpecial_Details_Scraping.py"])
    if platform.system() == 'Linux':
        os.chdir(r"/home/zsandark/_DEV/Python/py_26-30_projects")
        call(["python3.11", "27_TVMovie-TVSpecial_Details_Scraping_CP.py"])

# BANNER
print('\n')
k = 11
print((' Z-z-z '*k).center(terminal_columns))
print()
print(' Beecider '.center(terminal_columns))
print()
print((' Z-z-z '*k).center(terminal_columns))
print()

print('Which type of nectar should I collect for you?'.center(terminal_columns))
print('Movie(M) / Show-Series(S) / TV Movie(T) '.center(terminal_columns))

print()
# print('t'.ljust(len(' Z-z-z '*int(k/2))), ' ', end='')   # original - move the cursor to middle
print(''.rjust(int((terminal_columns/2)-1)), end='')  
n_type = input().lower()

while n_type not in ['m','s','t']:
    print()
    print('It`s a typo buddy. Try again: ', end='')
    n_type = input().lower()

if n_type == 'm':
    run_Movie()

if n_type == 's':
    run_Series()

if n_type == 't':
    run_TV_Movie_TV_Special()
