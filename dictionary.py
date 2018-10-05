# -*- coding: utf-8 -*-

#---- IMPORTS ----#
from easygui import *
import openpyxl

#---- FUNCTIIONS ----#
def menu():
    """ main menu to choose from dict search or add new word """
    msg = "Üdv a szótáramban. Mit szeretnél csinálni?"
    choices = ["Szavak keresése", "Új szó hozzáadása", "Kilépés"]
    title = "Peti koreai-magyar szótára"
    choice = buttonbox(msg=msg, title=title, choices=choices)

    if choice == "Szavak keresése":
        return 1
    elif choice == "Új szó hozzáadása":
        return 2
    elif choice == "Kilépés":
        return 3


def word_input():
    """ requests input of a word or part of a word """
    title = "Peti koreai-magyar szótára"
    word = ""
    while word == "" :
        word = enterbox(msg="A keresett szó: ", title=title)

    if word != None :
        word.strip()
    return word


def word_lookup(kor, hun, word):
    """ looks up if the word exists either in korean or in hungarian list, then
    puts both words in a 2D list """
    i = 0
    result = []
    # first: checking for exact match
    while i < len(hun):
        if word == hun[i]:
            key = hun[i]
            value = kor[i]
            i += 1
            result.append([key, value])

        elif word == kor[i]:
            key = kor[i]
            value = hun[i]
            i += 1
            result.append([key, value])

        else:
            i += 1

    # second: checking for partial match AND if it's not already in the result list
    # this way exact match(es) will be on the begining of the results
    i = 0
    while i < len(hun):        
        if word in hun[i] and not any(hun[i] in sublist for sublist in result):
            key = hun[i]
            value = kor[i]
            i += 1
            result.append([key, value])

        elif word in kor[i] and not any(hun[i] in sublist for sublist in result):
            key = kor[i]
            value = hun[i]
            i += 1
            result.append([key, value])
          
        else:
            i += 1
        
    return result


def result_output(result):
    """ creates a string of the 2D list, separated by '=' characters and with each word 
    pair in new line, then makes the output in a textbox window """
    title = "Peti koreai-magyar szótára"
    i = 0
    str_result = ""
    while i < len(result):
        str_result += result[i][0] + " = " + result[i][1] + "\n"
        i += 1

    if str_result == "":
        msgbox(msg="Nincs találat.", title=title)
        
    else:
        textbox(msg="A találat(ok):", title=title, text=str_result)


def load_dict_column(book, sheet, column):
    """ loads the given column of an excel sheet to a list """ 
    mylist = []
    for col in sheet[column]:
        mylist.append(col.value)

    return mylist


def new_word_input():
    """ asks the new korean and hungarian words in a multenterbox """
    msg = "Kérlek add meg az új szavakat:"
    names = ["Koreaiul:", "Magyarul:"]
    title = "Peti koreai-magyar szótára"

    values = multenterbox(msg=msg, title=title, fields=names)

    return values


def add_new_word(book, sheet, values, filename):
    """ opens the excel file and puts the new words into the first empty row """
    sheet.append(values)
    book.save(filename)


#---- MAIN PROGRAM ----#

# loading the dictionary file
filename = 'korhun_dict.xlsx'
book = openpyxl.load_workbook(filename=filename)
sheet = book['Sheet1']
kor = load_dict_column(book, sheet, 'A')
hun = load_dict_column(book, sheet, 'B')

# var for the menu choices
choice = 0

# while the exit button ('Kilépés') is not pressed loops the program
try: 
    while choice != 3 :
        choice = menu()

        if choice == 1 :        # word lookup
            word = word_input()
            if word == None:
                continue
            result = word_lookup(kor, hun, word)
            result_output(result)

        elif choice == 2 :      # add new word
            values = new_word_input()
            if values == None:
                continue
            add_new_word(book, sheet, values, filename)
            

# attribute error: when the program closes with 'word' is empty and .strip() has no attribute
except AttributeError:
    pass




