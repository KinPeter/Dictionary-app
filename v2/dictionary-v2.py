from tkinter import *
from backend import MyDict

class Window(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title('Koreai-Magyar Szótár')
        self.window.minsize(500,450)

        l1 = Label(window, text = 'Szó keresése')
        l1.pack(pady=(10,0))

        self.lookup = StringVar()
        self.e1 = Entry(window, textvariable=self.lookup, width=40)
        self.e1.pack()
        self.e1.bind('<Return>', self.search_command)

        b1 = Button(window, text = 'Keress', relief=GROOVE, command=self.search_command)
        b1.pack(pady=(5,10), ipadx=10)

        resultbox = Frame(window)
        resultbox.pack(expand=YES)
        self.tb = Text(resultbox, height=15, width=50)
        scr = Scrollbar(resultbox)
        self.tb.pack(side=LEFT, fill=BOTH, expand=YES)
        scr.pack(side=RIGHT, fill=Y)
        scr.config(command=self.tb.yview)
        self.tb.config(yscrollcommand=scr.set)

        l2 = Label(window, text='Új szó hozzáadása: ')
        l2.pack(pady=(10,0))

        addbox = Frame(window)
        addbox.pack()
        self.newkor = StringVar()
        self.e2 = Entry(addbox, textvariable=self.newkor, width=25)
        self.e2.pack(side=LEFT)
        self.e2.insert(END, '한국어')
        l3 = Label(addbox, text=' < - > ')
        l3.pack(side=LEFT)
        self.newhun = StringVar()
        self.e3 = Entry(addbox, textvariable=self.newhun, width=25)
        self.e3.pack(side=LEFT)
        self.e3.insert(END, 'magyar')
        self.e3.bind('<Return>', self.addnew_command)

        b2 = Button(window, text = 'Hozzáad', relief=GROOVE, command=self.addnew_command)
        b2.pack(pady=(5,10), ipadx=10)


    def search_command(self, event=None):
        word = self.lookup.get()
        if word != '':
            result = korhun.result_output(korhun.word_lookup(word.strip()))
        else:
            result = 'Nincs találat :('
        self.tb.delete('1.0', END)
        self.tb.insert('1.0', result)


    def addnew_command(self, event=None):
        newwords = (self.newkor.get(), self.newhun.get())
        korhun.add_new_word(newwords)


korhun = MyDict('korhun_dict.xlsx')
window = Tk()
Window(window)
window.mainloop()
