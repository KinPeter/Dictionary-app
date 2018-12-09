# -*- coding: utf-8 -*-
import openpyxl

class MyDict:

    def __init__(self, filename):
        """ loading the dictionary file """
        self.book = openpyxl.load_workbook(filename=filename)
        self.sheet = self.book['Sheet1']
        self.filename = filename
        self.kor = self.load_dict_column('A')
        self.hun = self.load_dict_column('B')

    def load_dict_column(self, column):
        """ loads the given column of the excel sheet to a list """
        mylist = []
        for col in self.sheet[column]:
            mylist.append(col.value)
        return mylist

    def word_lookup(self, word):
        """ looks up if the word exists either in korean or in hungarian list, then puts both words in a 2D list """
        i = 0
        result = []

        while i < len(self.hun):
            if word.lower() == self.hun[i].lower():
                result.append([self.hun[i], self.kor[i]])

            elif word.lower() == self.kor[i].lower():
                result.append([self.kor[i], self.hun[i]])
            i += 1

        i = 0
        while i < len(self.hun):
            if word.lower() in self.hun[i].lower() and not any(self.hun[i] in sublist for sublist in result):
                result.append([self.hun[i], self.kor[i]])

            elif word.lower() in self.kor[i].lower() and not any(self.hun[i] in sublist for sublist in result):
                result.append([self.kor[i], self.hun[i]])
            i += 1

        return result

    def result_output(self, result):
        """ creates a string of the 2D list, separated by '=' characters and with each word pair in new line """
        i = 0
        str_result = ""
        while i < len(result):
            str_result += result[i][0] + " = " + result[i][1] + "\n"
            i += 1
        return str_result

    def add_new_word(self, values):
        """ opens the excel file and puts the new words into the first empty row """
        self.sheet.append(values)
        self.book.save(self.filename)


#korhun = MyDict('korhun_dict.xlsx')

#print(korhun.result_output(korhun.word_lookup('fölött')))

#korhun.add_new_word(('teszt3', 'teszt4'))
